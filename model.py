import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import xgboost as xgb

st.write("""
# Car's Price Prediction App
This app predicts the **Car's Price** based on its input features!
""")
st.write('---')

# Loads the cleaned dataset
df = pd.read_csv('cleaned_full_data.csv', index_col=0)
X_df = df[['Make', 'Car Model', 'Model Year', 'Mileage', 'Rating', 'Fuel Type', 'City MPG', 'Highway MPG', 'Drivetrain',
           'Engine', 'Exterior Color',
           'Interior Color', 'Transmission', 'Num_ent_features', 'Num_safe_features']]
y_df = df.loc[:, 'Price']

# Sidebar
# Header of Specify Numerical and Categorical Input Parameters
st.sidebar.header('Specify Numerical Input Parameters')
st.write("**Specify Categorical Input Parameters**")


def user_input_features():
    Make = st.selectbox('Make', ('BMW',
                                 'Toyota',
                                 'INFINITI',
                                 'Mercedes-Benz',
                                 'Kia',
                                 'Volkswagen',
                                 'Porsche',
                                 'Acura',
                                 'Dodge',
                                 'GMC',
                                 'Ford',
                                 'Hyundai',
                                 'Audi',
                                 'Honda',
                                 'Lexus',
                                 'Chevrolet',
                                 'Jeep',
                                 'Subaru',
                                 'Volvo',
                                 'Maserati',
                                 'Mazda',
                                 'Alfa Romeo',
                                 'Lincoln',
                                 'Buick',
                                 'Nissan',
                                 'Land Rover',
                                 'Mitsubishi',
                                 'Chrysler',
                                 'RAM',
                                 'Cadillac',
                                 'Jaguar',
                                 'Tesla',
                                 'Genesis',
                                 'MINI Cooper',
                                 'Bentley',
                                 'Aston Martin',
                                 'FIAT',
                                 'Other',
                                 'Scion',
                                 'smart',
                                 'Hummer',
                                 'Pontiac',
                                 'Saturn'))
    Car_Model = st.selectbox("Car Model", ('330',
                                           'RAV4',
                                           'Q60',
                                           'GLS',
                                           'Optima',
                                           'GLE',
                                           'Tiguan',
                                           'Cayenne',
                                           'X3',
                                           'MDX',
                                           'Durango',
                                           '540',
                                           'Yukon',
                                           'Fiesta',
                                           'Tucson',
                                           'C',
                                           'X5',
                                           'A6',
                                           'E',
                                           'M550',
                                           'TSX',
                                           'Focus',
                                           'HR-V',
                                           'Charger',
                                           '440',
                                           'Fit',
                                           'Q7',
                                           'Journey',
                                           'RX',
                                           'Traverse',
                                           'QX60',
                                           'Cherokee',
                                           'Outback',
                                           'XC90',
                                           'C-HR',
                                           'Ghibli',
                                           '718',
                                           'AMG',
                                           'CR-V',
                                           'NX',
                                           'Grand',
                                           'WRX',
                                           'CX-5',
                                           'Romeo',
                                           'Pilot',
                                           'Aviator',
                                           'Regal',
                                           'Highlander',
                                           'Murano',
                                           'GLC',
                                           'Explorer',
                                           'Rover',
                                           'IS',
                                           'X2',
                                           'Outlander',
                                           'Pacifica',
                                           'Odyssey',
                                           'Telluride',
                                           'Malibu',
                                           'SQ5',
                                           'Fusion',
                                           'Jetta',
                                           'XC40',
                                           'GL',
                                           'Camaro',
                                           'Civic',
                                           'Forester',
                                           'QX80',
                                           '1500',
                                           'X4',
                                           'S60',
                                           'Rogue',
                                           '300',
                                           'GX',
                                           'MKC',
                                           'XC60',
                                           'Santa',
                                           'Tacoma',
                                           'A5',
                                           '350',
                                           'Mazda3',
                                           'Ascent',
                                           'Sentra',
                                           'TLX',
                                           'Atlas',
                                           '430',
                                           'Panamera',
                                           'S5',
                                           'Lancer',
                                           '740',
                                           'Q3',
                                           'Tahoe',
                                           '128',
                                           'Sienna',
                                           'Town',
                                           'A4',
                                           'Genesis',
                                           'LS',
                                           'X6',
                                           'Escalade',
                                           'Silverado',
                                           'Q5',
                                           'Sonata',
                                           'Accord',
                                           'F-TYPE',
                                           'Tundra',
                                           '328',
                                           'S4',
                                           'Other',
                                           'Sierra',
                                           'Challenger',
                                           'Q50',
                                           'Model',
                                           'X1',
                                           'Renegade',
                                           'Levante',
                                           'Q8',
                                           'Quattroporte',
                                           'GS',
                                           'CLS',
                                           'Wrangler',
                                           'ES',
                                           'ML',
                                           'Corolla',
                                           'XT5',
                                           'CX-9',
                                           'S',
                                           'XT4',
                                           'Equinox',
                                           'S90',
                                           'Crosstrek',
                                           'Terrain',
                                           'Acadia',
                                           'Macan',
                                           'Sportage',
                                           'Suburban',
                                           'Altima',
                                           'S6',
                                           'Golf',
                                           'Sorento',
                                           '4Runner',
                                           'Mustang',
                                           'F-PACE',
                                           'Encore',
                                           'Camry',
                                           'MX-5',
                                           'Kona',
                                           'Pathfinder',
                                           'V60',
                                           'Compass',
                                           'MKX',
                                           'Expedition',
                                           'GLA',
                                           '530',
                                           'G80',
                                           'CLA',
                                           'Continental',
                                           'A8',
                                           'LT',
                                           'A7',
                                           'Patriot',
                                           'Juke',
                                           'F-150',
                                           'MKZ',
                                           'Base',
                                           'Land',
                                           'Elantra',
                                           'Escape',
                                           'Clubman',
                                           '428',
                                           'Enclave',
                                           'GLB',
                                           'Passport',
                                           'RDX',
                                           'Passat',
                                           '230',
                                           'Frontier',
                                           'Transit-250',
                                           'G70',
                                           'Corvette',
                                           '228',
                                           'CT6',
                                           'Armada',
                                           'Nitro',
                                           'Blazer',
                                           '320',
                                           'A',
                                           'Palisade',
                                           'X7',
                                           '2500',
                                           'Canyon',
                                           'A3',
                                           '911',
                                           'ILX',
                                           '340',
                                           'S3',
                                           'M340',
                                           'SL',
                                           'Trax',
                                           'Maxima',
                                           'XTS',
                                           'Sedona',
                                           'S7',
                                           'S80',
                                           'XE',
                                           '2.5i',
                                           'RS',
                                           'Ridgeline',
                                           'Martin',
                                           'SRX',
                                           'LX',
                                           'Cube',
                                           'QX50',
                                           'M2',
                                           'Gladiator',
                                           'Colorado',
                                           'Impreza',
                                           '535',
                                           'M5',
                                           'CTS-V',
                                           '750',
                                           '550',
                                           'Edge',
                                           'M4',
                                           'i3',
                                           'XT6',
                                           'Taurus',
                                           'Mazda6',
                                           'Bolt',
                                           'Nautilus',
                                           'Voyager',
                                           '640',
                                           '500C',
                                           'Soul',
                                           'Azera',
                                           'ATS',
                                           'XJ',
                                           'RLX',
                                           '328d',
                                           '500X',
                                           'Metris',
                                           'Countryman',
                                           'MKT',
                                           'CX-3',
                                           'E-PACE',
                                           'Flex',
                                           'Flying',
                                           '650',
                                           'M3',
                                           'QX30',
                                           'TL',
                                           'Forte',
                                           'M240',
                                           'GLK',
                                           'CT',
                                           'Legacy',
                                           'ProMaster',
                                           'RC',
                                           'Beetle',
                                           'Prius',
                                           'Stinger',
                                           '335',
                                           'Kicks',
                                           'QX70',
                                           'CTS',
                                           'Navigator',
                                           '500',
                                           'Supra',
                                           '528',
                                           'V90',
                                           'Touareg',
                                           'G',
                                           'Shelby',
                                           'Dart',
                                           'M235',
                                           'Venue',
                                           'i8',
                                           'Titan',
                                           '530e',
                                           'F-250',
                                           'Hardtop',
                                           'Sonic',
                                           'Impala',
                                           'e-Golf',
                                           'MKS',
                                           'Venza',
                                           'UX',
                                           'Quest',
                                           'CT4',
                                           'Lucerne',
                                           'Versa',
                                           '2.5',
                                           'Eclipse',
                                           'TT',
                                           'Z4',
                                           'Envision',
                                           'Q70',
                                           'ATS-V',
                                           '200',
                                           'Accent',
                                           'EX35',
                                           'LaCrosse',
                                           'Convertible',
                                           'XF',
                                           'Cayman',
                                           '330e',
                                           'EcoSport',
                                           'Cascada',
                                           'Cruze',
                                           'Niro',
                                           'Avenger',
                                           'Mirage',
                                           'BRZ',
                                           'Ranger',
                                           '370Z',
                                           'Sequoia',
                                           'Yaris',
                                           'SE',
                                           'G90',
                                           'Mazda5',
                                           'GTI',
                                           'Avalon',
                                           'Volt',
                                           'S500',
                                           'tC',
                                           'SLC',
                                           'C300',
                                           'allroad',
                                           'CX-30',
                                           'Corsair',
                                           'Cooper',
                                           'XV',
                                           'SS',
                                           'K900',
                                           'Arteon',
                                           'Spark',
                                           'C-Max',
                                           '435',
                                           'e-tron',
                                           'XK',
                                           'ForTwo',
                                           'RL',
                                           'M440',
                                           'DTS',
                                           'CT5',
                                           'M6',
                                           'F-350',
                                           'S40',
                                           'Express',
                                           'Q70L',
                                           'FJ',
                                           'Transit',
                                           'G37',
                                           'Ram',
                                           'Leaf',
                                           'Premium',
                                           'Boxster',
                                           'Savana',
                                           'Insight',
                                           'Liberty',
                                           'XC70',
                                           'GT-R',
                                           'LC',
                                           'M37',
                                           'JX35',
                                           'Veloster',
                                           'Captiva',
                                           'R8',
                                           'TTS',
                                           'CL',
                                           'SLT',
                                           'Cadenza',
                                           'Xterra',
                                           'Paceman',
                                           '300C',
                                           'FR-S',
                                           'H3',
                                           'Eos',
                                           'S8',
                                           'xD',
                                           '740e',
                                           'SL500',
                                           'iM',
                                           'Ioniq',
                                           'CC',
                                           'GranTurismo',
                                           'Uplander',
                                           'QX56',
                                           '500L',
                                           'Commander',
                                           'Seltos',
                                           'TrailBlazer',
                                           'Routan',
                                           'Bronco',
                                           'H2',
                                           'Verano',
                                           'SEL',
                                           '500e',
                                           'xB',
                                           'M760',
                                           'ALPINA',
                                           'NV200',
                                           'FX35',
                                           'Sprinter',
                                           'Vue',
                                           'Rio5',
                                           'F-450',
                                           '124',
                                           'Clarity',
                                           'K5',
                                           'CX-7',
                                           'Avalanche',
                                           'Limited',
                                           'Rio',
                                           'SLK',
                                           '3500',
                                           'SV',
                                           'Transit-350',
                                           'NV',
                                           'Transit-150',
                                           'Sport',
                                           'I-PACE',
                                           'SC',
                                           'C250',
                                           'CLK320',
                                           'Lexus',
                                           '350Z',
                                           '535d',
                                           'New',
                                           'G37x',
                                           'B',
                                           'PT',
                                           'Caliber',
                                           'Mirai',
                                           'M850',
                                           'Element',
                                           'G6'))
    Model_Year = st.sidebar.slider("Year", 2001, 2022, 2018)
    Mileage = st.sidebar.slider("Mileage", 1, 200000, 10000)
    Rating = st.sidebar.slider("Rating", 1.0, 5.0, 4.7)
    Fuel_Type = st.selectbox('Fuel Type', ('Gasoline', 'E85 Flex Fuel', 'Hybrid', 'Diesel', 'Electric'))
    City_MPG = st.sidebar.slider("City MPG", 0, 210, 16)
    Highway_MPG = st.sidebar.slider("Highway MPG", 0, 420, 25)
    Drivetrain = st.selectbox('Drivetrain', ('AWD', 'FWD', '4WD', 'RWD'))
    Engine = st.selectbox('Engine', ('2.0L',
                                     '2.5L',
                                     '3.0L',
                                     '2.4L',
                                     '3.5L',
                                     '3.7L',
                                     '5.7L',
                                     '3.6L',
                                     '6.2L',
                                     '1.6L',
                                     '4.4L',
                                     '1.8L',
                                     '1.5L',
                                     '4.7L',
                                     '3.2L',
                                     '2.3L',
                                     '5.0L',
                                     '3.8L',
                                     'Other',
                                     '1.4L',
                                     '5.6L',
                                     '4.6L',
                                     'Regular Unleaded I-4 2.4 L/144',
                                     '5.5L',
                                     '2.7L',
                                     '4.0L',
                                     '5.3L',
                                     '6.4L',
                                     'Electric',
                                     'V6',
                                     'Premium',
                                     '3.3L',
                                     'I4',
                                     'Intercooled Turbo Premium Unleaded I-4 2.0 L/121',
                                     '4.3L',
                                     'Regular Unleaded V-6 3.6 L/220',
                                     '6.7L',
                                     'Intercooled Turbo Premium Unleaded I-4 2.0 L/122',
                                     '6.0L',
                                     'Regular Unleaded V-6 3.5 L/212',
                                     'Regular Unleaded I-4 2.5 L/152',
                                     'Gas',
                                     'Regular Unleaded V-8 5.7 L/345',
                                     'Regular Unleaded V-6 3.5 L/211',
                                     '1.3L',
                                     'Turbocharged',
                                     'Twin',
                                     'Intercooled Turbo Regular Unleaded I-4 1.5 L/91',
                                     '1.0L',
                                     'Intercooled Turbo Premium Unleaded I-6 3.0 L/183',
                                     '5.4L',
                                     'Gas/Ethanol',
                                     '6.6L',
                                     'Intercooled Supercharger Premium Unleaded V-6 3.0 L/183',
                                     'Regular Unleaded V-6 4.0 L/241',
                                     '1.2L',
                                     '5.2L',
                                     'Regular Unleaded H-4 2.5 L/152'))
    Exterior_Color = st.selectbox('Exterior Color',
                                  ('Black', 'Gray', 'White', 'Blue', 'Silver', 'Metallic', 'Red', 'Other'))
    Interior_Color = st.selectbox('Interior Color', ('Black', 'Graphite', 'Other', 'Gray', 'Ebony', 'Charcoal'))
    Transmission = st.selectbox('Transmission', ('Automatic', 'Manual'))
    Num_ent_features = st.sidebar.slider('Number of entertainment features', 1, 10, 2)
    Num_safe_features = st.sidebar.slider('Number of safety features', 1, 10, 2)

    data = {'Make': Make,
            'Car Model': Car_Model,
            'Model Year': Model_Year,
            'Mileage': Mileage,
            'Rating': Rating,
            'Fuel Type': Fuel_Type,
            'City MPG': City_MPG,
            'Highway MPG': Highway_MPG,
            'Drivetrain': Drivetrain,
            'Engine': Engine,
            'Exterior Color': Exterior_Color,
            'Interior Color': Interior_Color,
            'Transmission': Transmission,
            'Num_ent_features': Num_ent_features,
            'Num_safe_features': Num_safe_features
            }
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()
new_df = pd.concat([X_df, df])
# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Build Regression Model
#model = LinearRegression()
model = joblib.load('trained_lin_model.pkl')
#model.fit(pd.get_dummies(X_df, drop_first=True), y_df)
# Apply Model to Make Prediction
#prediction = model.predict(new_df)[-1]
prediction = format(model.predict(pd.get_dummies(new_df, drop_first=True))[-1], '.2f')

st.header('Prediction')
st.write('The {} {} {}-{} car with {} miles with the engine of {} is predicted to be **${}**'.format(
    df['Model Year'].values[0], df.Drivetrain.values[0], df.Make.values[0], df['Car Model'].values[0],
    df.Mileage.values[0], df.Engine.values[0], prediction))
st.write('---')
