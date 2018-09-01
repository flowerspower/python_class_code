# This code is modified from scikit-learn source code

from os import listdir, makedirs, remove
from os.path import join, exists, isdir

import logging
import numpy as np

from PIL import Image
from scipy.misc.pilutil import fromimage
from scipy.misc import imresize

logger = logging.getLogger(__name__)

class Bunch(dict):
    """Container object for datasets

    Dictionary-like object that exposes its keys as attributes.

    >>> b = Bunch(a=1, b=2)
    >>> b['b']
    2
    >>> b.b
    2
    >>> b.a = 3
    >>> b['a']
    3
    >>> b.c = 6
    >>> b['c']
    6

    """

    def __init__(self, **kwargs):
        super(Bunch, self).__init__(kwargs)

    def __setattr__(self, key, value):
        self[key] = value

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setstate__(self, state):
        # Bunch pickles generated with scikit-learn 0.16.* have an non
        # empty __dict__. This causes a surprising behaviour when
        # loading these pickles scikit-learn 0.17: reading bunch.key
        # uses __dict__ but assigning to bunch.key use __setattr__ and
        # only changes bunch['key']. More details can be found at:
        # https://github.com/scikit-learn/scikit-learn/issues/6196.
        # Overriding __setstate__ to be a noop has the effect of
        # ignoring the pickled __dict__
        pass

def read_jpg(file_path):
    image = Image.open(file_path)
    if hasattr(image, "_getexif"):
        orientation = 0x0112
        exif = image._getexif()
        if exif is not None:
            orientation = exif[orientation]
            rotations = {
                3: Image.ROTATE_180,
                6: Image.ROTATE_270,
                8: Image.ROTATE_90
            }
            if orientation in rotations:
                image = image.transpose(rotations[orientation])
    return fromimage(image, flatten = False, mode = None)

def _load_imgs(file_paths, slice_, color, resize):
    """Internally used to load images"""
    # compute the portion of the images to load to respect the slice_ parameter
    # given by the caller
    default_slice = (slice(0, 250), slice(0, 250))
    if slice_ is None:
        slice_ = default_slice
    else:
        slice_ = tuple(s or ds for s, ds in zip(slice_, default_slice))

    h_slice, w_slice = slice_
    h = (h_slice.stop - h_slice.start) // (h_slice.step or 1)
    w = (w_slice.stop - w_slice.start) // (w_slice.step or 1)

    # allocate some contiguous memory to host the decoded image slices
    n_faces = len(file_paths)
    if not color:
        faces = np.zeros((n_faces, h, w), dtype=np.float32)
    else:
        faces = np.zeros((n_faces, h, w, 3), dtype=np.float32)

    # iterate over the collected file path to load the jpeg files as numpy
    # arrays
    for i, file_path in enumerate(file_paths):
        if i % 1000 == 0:
            logger.debug("Loading face #%05d / %05d", i + 1, n_faces)

        # Checks if jpeg reading worked. Refer to issue #3594 for more
        # details.
        img = read_jpg(file_path)
        if img.ndim is 0:
            raise RuntimeError("Failed to read the image file %s, "
                               "Please make sure that libjpeg is installed"
                               % file_path)
        face = np.asarray(img, dtype=np.float32)
        face /= 255.0  # scale uint8 coded colors to the [0.0, 1.0] floats

        if resize is not None:
            face = imresize(face, (resize, resize))
            face = np.asarray(face[slice_], dtype=np.float32)

        if not color:
            # average the color channels to compute a gray levels
            # representation
            face = face.mean(axis=2)

        faces[i, ...] = face

    return faces


def _fetch_faces(data_folder_path, slice_=None, color=False, resize=None):
    person_names, file_paths = [], []
    for person_name in sorted(listdir(data_folder_path)):
        folder_path = join(data_folder_path, person_name)
        if not isdir(folder_path):
            continue
        paths = [join(folder_path, f) for f in sorted(listdir(folder_path))]
        n_pictures = len(paths)
        person_name = person_name.replace('_', ' ')
        person_names.extend([person_name] * n_pictures)
        file_paths.extend(paths)

    n_faces = len(file_paths)
    target_names = np.unique(person_names)
    target = np.searchsorted(target_names, person_names)

    faces = _load_imgs(file_paths, slice_, color, resize)

    # shuffle the faces with a deterministic RNG scheme to avoid having
    # all faces of the same person in a row, as it would break some
    # cross validation and learning algorithms such as SGD and online
    # k-means that make an IID assumption

    indices = np.arange(n_faces)
    np.random.RandomState(42).shuffle(indices)
    faces, target = faces[indices], target[indices]
    return faces, target, target_names


def fetch_faces(data_folder_path, resize=250, color=False,
                     slice_=(slice(70, 195), slice(78, 172))):
    # load and memoize the pairs as np arrays
    faces, target, target_names = _fetch_faces(
        data_folder_path, resize=resize, color=color, slice_=slice_)

    # pack the results as a Bunch instance
    return Bunch(data=faces.reshape(len(faces), -1), images=faces,
                 target=target, target_names=target_names,
                 DESCR="Kids faces dataset")


def load_one_face(jpeg_file, resize = 250, color=False, slice_=(slice(70, 195), slice(78, 172))):
    img = read_jpg(jpeg_file)
    if img.ndim is 0:
        raise RuntimeError("Failed to read the image file %s, "
                           "Please make sure that libjpeg is installed"
                           % jpeg_file)
    face = np.asarray(img, dtype=np.float32)
    face /= 255.0  # scale uint8 coded colors to the [0.0, 1.0] floats

    if resize is not None:
        face = imresize(face, (resize, resize))
        face = np.asarray(face[slice_], dtype=np.float32)

    if not color:
        # average the color channels to compute a gray levels
        # representation
        face = face.mean(axis=2)

    return face

# print fetch_faces('/Users/wyh/faces')