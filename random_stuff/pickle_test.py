# Pickles are green
import pickle

kids = {
    'Sean': 'Slimey grimey fat pink naked mole rat.',
    'Jerry': 'Poop. Pee. Toilet. Stinky. Overweight.',
    'Sophia': 'Unicorn! Awesome! Amazing! A+! A VIP!',
    'Daniel': 'Stupid okay-ish little annoying snail.'
}
output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(kids, output)

output.close()

pkl_file = open('data.pkl', 'rb')

data2 = pickle.load(pkl_file)

pkl_file.close()

print data2