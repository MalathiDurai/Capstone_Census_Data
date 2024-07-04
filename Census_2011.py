# %%
import pandas as pd
import pymongo
import streamlit as st
import cx_Oracle


# %%
#Connect to Oracle DB
def connect_oracledb():
    try:
        hostname = 'localhost'
        port = '1521'
        user = 'hr'
        password = 'hr_new2'
        sid = 'xe'

        dsn = cx_Oracle.makedsn(hostname, port, sid=sid)
        connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)

        print("RDBMS - Oracle DB connection established successfully.")
        return connection
    except cx_Oracle.DatabaseError as err:
        print(f"Error connecting to Oracle DB: {err}")
        st.error(f"Error connecting to Oracle DB: {err}")
        return None


#connect_oracledb()

# %%
# Connect to MongoDB
def connect_mongo():
    try:
        connection_string = "mongodb://localhost:27017"
        client = pymongo.MongoClient(connection_string)
        db = client['census']
        collection = db["census"]
        print("MongoDB connection established successfully.")
        return collection
    except Exception as e:
        print(f"An error occurred while connecting to MongoDB: {e}")
        st.error(f"An error occurred while connecting to MongoDB: {e}")
        return None


#connect_mongo()

# %%
def fetch_data():
    try:
        file_path = "census_2011.xlsx"
        df = pd.read_excel(file_path)
        print("Data fetched from Git path successfully.")
    except Exception as e:
        print(f"An error occurred while fetching local files: {e}")
        return None
    return df


#df = fetch_data()


# %%
# Rename the Column names by removing spaces and reducing the size effectively
def rename_columns(df):
    #removing spaces between column names
    df.columns = df.columns.str.replace(' ', '_')
    # Rename the columns as per standard format
    column_mapping = {
        'District_code': 'District_Code',
        'State_name': 'State_UT',
        'District_name': 'District_Name',
        'Population': 'Population',
        'Male': 'Male',
        'Female': 'Female',
        'Literate': 'Literate',
        'Male_Literate': 'MaleLiterate',
        'Female_Literate': 'FemaleLiterate',
        'SC': 'SC',
        'Male_SC': 'MaleSC',
        'Female_SC': 'FemaleSC',
        'ST': 'ST',
        'Male_ST': 'MaleST',
        'Female_ST': 'FemaleST',
        'Workers': 'Workers',
        'Male_Workers': 'MaleWorkers',
        'Female_Workers': 'FemaleWorkers',
        'Main_Workers': 'MainWorkers',
        'Marginal_Workers': 'MarginalWorkers',
        'Non_Workers': 'NonWorkers',
        'Cultivator_Workers': 'CultivatorWorkers',
        'Agricultural_Workers': 'AgrWorkers',
        'Household_Workers': 'HHWorkers',
        'Other_Workers': 'OtherWorkers',
        'Hindus': 'Hindus',
        'Muslims': 'Muslims',
        'Christians': 'Christians',
        'Sikhs': 'Sikhs',
        'Buddhists': 'Buddhists',
        'Jains': 'Jains',
        'Others_Religions': 'Others_Religions',
        'Religion_Not_Stated': 'RelNotStated',
        'LPG_or_PNG_Households': 'LPGHH',
        'Housholds_with_Electric_Lighting': 'ElecLightHH',
        'Households_with_Internet': 'InternetHH',
        'Households_with_Computer': 'ComputerHH',
        'Rural_Households': 'RuralHH',
        'Urban_Households': 'UrbanHH',
        'Households': 'TotalHH',
        'Below_Primary_Education': 'BelowPrimaryEdu',
        'Primary_Education': 'PrimaryEdu',
        'Middle_Education': 'MiddleEdu',
        'Secondary_Education': 'SecondaryEdu',
        'Higher_Education': 'HigherEdu',
        'Graduate_Education': 'GradEdu',
        'Other_Education': 'OtherEdu',
        'Literate_Education': 'LitEdu',
        'Illiterate_Education': 'IllitEdu',
        'Total_Education': 'TotalEdu',
        'Age_Group_0_29': 'Young_and_Adult',
        'Age_Group_30_49': 'Middle_Aged',
        'Age_Group_50': 'Senior_Citizen',
        'Age_not_stated': 'Age_Not_Stated',
        'Households_with_Bicycle': 'BicycleHH',
        'Households_with_Car_Jeep_Van': 'CarJeepVanHH',
        'Households_with_Radio_Transistor': 'RadioTransHH',
        'Households_with_Scooter_Motorcycle_Moped': 'ScooterMotorMopedHH',
        'Households_with_Telephone_Mobile_Phone_Landline_only': 'PhoneLandlineHH',
        'Households_with_Telephone_Mobile_Phone_Mobile_only': 'MobileOnlyHH',
        'Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car': 'TVCompLaptopHH',
        'Households_with_Television': 'TVHH',
        'Households_with_Telephone_Mobile_Phone': 'PhoneHH',
        'Households_with_Telephone_Mobile_Phone_Both': 'PhoneBothHH',
        'Condition_of_occupied_census_houses_Dilapidated_Households': 'DilapHouseHH',
        'Households_with_separate_kitchen_Cooking_inside_house': 'SepKitchenHH',
        'Having_bathing_facility_Total_Households': 'BathFacHH',
        'Having_latrine_facility_within_the_premises_Total_Households': 'LatrineFacHH',
        'Ownership_Owned_Households': 'OwnedHH',
        'Ownership_Rented_Households': 'RentedHH',
        'Type_of_bathing_facility_Enclosure_without_roof_Households': 'BathFacEnclosureHH',
        'Type_of_fuel_used_for_cooking_Any_other_Households': 'OtherFuelHH',
        'Type_of_latrine_facility_Pit_latrine_Households': 'PitLatrineHH',
        'Type_of_latrine_facility_Other_latrine_Households': 'OtherLatrineHH',
        'Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households': 'NightSoilLatrineHH',
        'Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households': 'FlushLatrineHH',
        'Not_having_bathing_facility_within_the_premises_Total_Households': 'NoBathFacHH',
        'Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households': 'NoLatrineFacHH',
        'Main_source_of_drinking_water_Un_covered_well_Households': 'UncoveredWellWaterHH',
        'Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households': 'HandpumpWaterHH',
        'Main_source_of_drinking_water_Spring_Households': 'SpringWaterHH',
        'Main_source_of_drinking_water_River_Canal_Households': 'RiverCanalWaterHH',
        'Main_source_of_drinking_water_Other_sources_Households': 'OtherWaterHH',
        'Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households': 'OtherWaterHH_River',
        'Location_of_drinking_water_source_Near_the_premises_Households': 'NearPremisesWaterHH',
        'Location_of_drinking_water_source_Within_the_premises_Households': 'WithinPremisesWaterHH',
        'Main_source_of_drinking_water_Tank_Pond_Lake_Households': 'PondLakeWaterHH',
        'Main_source_of_drinking_water_Tapwater_Households': 'TapWaterHH',
        'Main_source_of_drinking_water_Tubewell_Borehole_Households': 'BoreholeWaterHH',
        'Household_size_1_person_Households': 'HHSize1Person',
        'Household_size_2_persons_Households': 'HHSize2Persons',
        'Household_size_1_to_2_persons': 'HHSize1To2Persons',
        'Household_size_3_persons_Households': 'HHSize3Persons',
        'Household_size_3_to_5_persons_Households': 'HHSize3To5Persons',
        'Household_size_4_persons_Households': 'HHSize4Persons',
        'Household_size_5_persons_Households': 'HHSize5Persons',
        'Household_size_6_8_persons_Households': 'HHSize6_8Persons',
        'Household_size_9_persons_and_above_Households': 'HHSize9AbovePersons',
        'Location_of_drinking_water_source_Away_Households': 'AwayWaterSourceHH',
        'Married_couples_1_Households': 'MarriedCouple1HH',
        'Married_couples_2_Households': 'MarriedCouple2HH',
        'Married_couples_3_Households': 'MarriedCouple3HH',
        'Married_couples_3_or_more_Households': 'MarriedCouple3OrMoreHH',
        'Married_couples_4_Households': 'MarriedCouple4HH',
        'Married_couples_5__Households': 'MarriedCouple5HH',
        'Married_couples_None_Households': 'MarriedCoupleNoneHH',
        'Power_Parity_Less_than_Rs_45000': 'PowerParityLess45000',
        'Power_Parity_Rs_45000_90000': 'PowerParity45000_90000',
        'Power_Parity_Rs_90000_150000': 'PowerParity90000_150000',
        'Power_Parity_Rs_45000_150000': 'PowerParity45000_150000',
        'Power_Parity_Rs_150000_240000': 'PowerParity150000_240000',
        'Power_Parity_Rs_240000_330000': 'PowerParity240000_330000',
        'Power_Parity_Rs_150000_330000': 'PowerParity150000_330000',
        'Power_Parity_Rs_330000_425000': 'PowerParity330000_425000',
        'Power_Parity_Rs_425000_545000': 'PowerParity425000_545000',
        'Power_Parity_Rs_330000_545000': 'PowerParity330000_545000',
        'Power_Parity_Above_Rs_545000': 'PowerParityAbove545000',
        'Total_Power_Parity': 'TotalPowerParity'
    }

    # Rename the columns in the DataFrame
    df = df.rename(columns=column_mapping)
    return df


#df = rename_columns(df)

# %%
# Standardizing State/UT Names
# Function to format the state names
def state_name_formatting(df):
    def capitalize_st(name):
        words = name.split()
        return ' '.join([word.capitalize() if word.lower() != 'and' else word.lower() for word in words])

    df["State_UT"] = df["State_UT"].apply(capitalize_st)

    # Change the state names to Ladakh
    ladakh_districts = ["Leh(Ladakh)", "Kargil"]
    df.loc[df["District_Name"].isin(ladakh_districts), "State_UT"] = "Ladakh"

    # Change the state names to Telangana
    with open('Telangana.txt') as file:
        telangana_districts = file.read().splitlines()

    df.loc[df["District_Name"].isin(telangana_districts), "State_UT"] = "Telangana"
    return df


#df = state_name_formatting(df)


# %%
# Analyzing and filling the missing values with valid data
def null_value_percent_filling(df):
    def null_percentage(df):
        null_percentage = (df.isnull().mean() * 100).round(2).astype(str) + '%'
        return null_percentage

    # missing data percentage before filling
    null_percentage_before = null_percentage(df)

    def fill_null_values(df):
        # fill Population column
        def calculate_population_count(row):
            if row["Male"] == 0:
                return row["Young_and_Adult"] + row["Middle_Aged"] + row["Senior_Citizen"] + row["Age_Not_Stated"]
            else:
                return row["Male"] + row["Female"]

        df["Population"] = df["Population"].fillna(df.apply(calculate_population_count, axis=1))

        # fill Male column
        df["Male"] = df["Male"].fillna(df["Population"] - df["Female"])

        # fill Female column
        df["Female"] = df["Female"].fillna(df["Population"] - df["Male"])

        # fill Literate Column
        df["Literate"] = df["Literate"].fillna(df["MaleLiterate"] + df["FemaleLiterate"])

        # fill Male_Literate Column
        df["MaleLiterate"] = df["MaleLiterate"].fillna(df["Literate"] - df["FemaleLiterate"])

        # fill Female_Literate Column
        df["FemaleLiterate"] = df["FemaleLiterate"].fillna(df["Literate"] - df["MaleLiterate"])

        # fill Young_and_Adult Column
        df["Young_and_Adult"] = df["Young_and_Adult"].fillna(
            df["Population"] - df["Middle_Aged"] - df["Senior_Citizen"] - df["Age_Not_Stated"])

        # fill Middle_Aged Column
        df["Middle_Aged"] = df["Middle_Aged"].fillna(
            df["Population"] - df["Young_and_Adult"] - df["Senior_Citizen"] - df["Age_Not_Stated"])

        # fill Senior_Citizen Column
        df["Senior_Citizen"] = df["Senior_Citizen"].fillna(
            df["Population"] - df["Young_and_Adult"] - df["Middle_Aged"] - df["Age_Not_Stated"])

        # fill Age_Not_Stated Column
        df["Age_Not_Stated"] = df["Age_Not_Stated"].fillna(
            df["Population"] - df["Young_and_Adult"] - df["Middle_Aged"] - df["Senior_Citizen"])

        return df

    df_updated = fill_null_values(df)

    null_percentage_after = null_percentage(df_updated)

    # Compare the percentages before and after
    comparison = pd.DataFrame({
        'Before': null_percentage_before,
        'After': null_percentage_after,
        'Difference': null_percentage_before.str.rstrip('%').astype(float) - null_percentage_after.str.rstrip(
            '%').astype(float)
    }).sort_values(by='Difference', ascending=False)

    return df_updated, comparison


#df_updated, comparison = null_value_percent_filling(df)


# %%
# Save Data to MongoDB
def data_load_into_mongodb(df_updated):
    try:
        # Convert DataFrame to dictionary format
        data_dict = df_updated.to_dict(orient='records')
        # Insert data into MongoDB
        connect_mongo().insert_many(data_dict)
        print("Data inserted into MongoDB successfully.")

        def null_value_correction_in_mongodb():
            import pymongo, math

            mongodb_connection = connect_mongo()
            documents = mongodb_connection.find()

            for document in documents:
                update_dict = {}
                for key, value in document.items():
                    if isinstance(value, float) and math.isnan(value):
                        update_dict[key] = 0.0

                # Update the document if any null values were found
                if update_dict:
                    mongodb_connection.update_one({"_id": document["_id"]}, {"$set": update_dict})

            print("Null value conversion completed")

        null_value_correction_in_mongodb()

    except Exception as e:
        print(f"An error occurred while loading data to MongoDB: {e}")


#data_load_into_mongodb(df_updated)

# %%
def rdbms_table_creation():
    try:
        # Connect to Oracle DB
        with connect_oracledb() as connection:
            if connection:
                # Create a cursor object using context manager
                with connection.cursor() as cursor:
                    # Defining table drop and creation queries
                    table_queries = [
                        """ALTER TABLE Demographics DROP CONSTRAINT fk_district_code_Geo""",
                        """ALTER TABLE Demographics DROP CONSTRAINT fk_district_code_hh""",
                        """DROP TABLE Districts""",
                        """DROP TABLE Demographics""",
                        """DROP TABLE Household""",
                        """CREATE SEQUENCE demo_sequence
                            START WITH 1
                            INCREMENT BY 1
                            NOMAXVALUE
                            NOCYCLE
                        """,
                        """CREATE SEQUENCE hh_sequence
                            START WITH 1
                            INCREMENT BY 1
                            NOCYCLE
                        """,
                        """
                        CREATE TABLE Districts (
                            District_Code NUMBER PRIMARY KEY,
                            State_UT VARCHAR2(50) NOT NULL,
                            District_Name VARCHAR2(50) NOT NULL,
                            Population NUMBER
                        )
                        """,
                        """
                        CREATE TABLE Demographics (
                            Demo_ID NUMBER PRIMARY KEY,
                            District_Code NUMBER NOT NULL,
                            Male NUMBER,
                            Female NUMBER,
                            Literate NUMBER,
                            MaleLiterate NUMBER,
                            FemaleLiterate NUMBER,
                            SC NUMBER,
                            MaleSC NUMBER,
                            FemaleSC NUMBER,
                            ST NUMBER,
                            MaleST NUMBER,
                            FemaleST NUMBER,
                            BelowPrimaryEdu NUMBER,
                            PrimaryEdu NUMBER,
                            MiddleEdu NUMBER,
                            SecondaryEdu NUMBER,
                            HigherEdu NUMBER,
                            GradEdu NUMBER,
                            OtherEdu NUMBER,
                            LitEdu NUMBER,
                            IllitEdu NUMBER,
                            TotalEdu NUMBER,
                            Workers NUMBER,
                            MaleWorkers NUMBER,
                            FemaleWorkers NUMBER,
                            MainWorkers NUMBER,
                            MarginalWorkers NUMBER,
                            NonWorkers NUMBER,
                            CultivatorWorkers NUMBER,
                            AgrWorkers NUMBER,
                            HHWorkers NUMBER,
                            OtherWorkers NUMBER,
                            Hindus NUMBER,
                            Muslims NUMBER,
                            Christians NUMBER,
                            Sikhs NUMBER,
                            Buddhists NUMBER,
                            Jains NUMBER,
                            Others_Religions NUMBER,
                            RelNotStated NUMBER,
                            Young_and_Adult NUMBER,
                            Middle_Aged NUMBER,
                            Senior_Citizen NUMBER,
                            Age_Not_Stated NUMBER,
                            CONSTRAINT fk_district_code_Geo FOREIGN KEY (District_Code) REFERENCES Districts (District_Code)
                        )
                        """,
                        """
                        CREATE TABLE Household (
                            Household_ID NUMBER PRIMARY KEY,
                            District_Code NUMBER,
                            LPGHH NUMBER,
                            ElecLightHH NUMBER,
                            InternetHH NUMBER,
                            ComputerHH NUMBER,
                            RuralHH NUMBER,
                            UrbanHH NUMBER,
                            TotalHH NUMBER,
                            BicycleHH NUMBER,
                            CarJeepVanHH NUMBER,
                            RadioTransHH NUMBER,
                            ScooterMotorMopedHH NUMBER,
                            PhoneLandlineHH NUMBER,
                            MobileOnlyHH NUMBER,
                            TVCompLaptopHH NUMBER,
                            TVHH NUMBER,
                            PhoneHH NUMBER,
                            PhoneBothHH NUMBER,
                            DilapHouseHH NUMBER,
                            SepKitchenHH NUMBER,
                            BathFacHH NUMBER,
                            LatrineFacHH NUMBER,
                            OwnedHH NUMBER,
                            RentedHH NUMBER,
                            BathFacEnclosureHH NUMBER,
                            OtherFuelHH NUMBER,
                            PitLatrineHH NUMBER,
                            OtherLatrineHH NUMBER,
                            NightSoilLatrineHH NUMBER,
                            FlushLatrineHH NUMBER,
                            NoBathFacHH NUMBER,
                            NoLatrineFacHH NUMBER,
                            UncoveredWellWaterHH NUMBER,
                            HandpumpWaterHH NUMBER,
                            SpringWaterHH NUMBER,
                            RiverCanalWaterHH NUMBER,
                            OtherWaterHH NUMBER,
                            OtherWaterHH_River NUMBER,
                            NearPremisesWaterHH NUMBER,
                            WithinPremisesWaterHH NUMBER,
                            PondLakeWaterHH NUMBER,
                            TapWaterHH NUMBER,
                            BoreholeWaterHH NUMBER,
                            HHSize1Person NUMBER,
                            HHSize2Persons NUMBER,
                            HHSize1To2Persons NUMBER,
                            HHSize3Persons NUMBER,
                            HHSize3To5Persons NUMBER,
                            HHSize4Persons NUMBER,
                            HHSize5Persons NUMBER,
                            HHSize6_8Persons NUMBER,
                            HHSize9AbovePersons NUMBER,
                            AwayWaterSourceHH NUMBER,
                            MarriedCouple1HH NUMBER,
                            MarriedCouple2HH NUMBER,
                            MarriedCouple3HH NUMBER,
                            MarriedCouple3OrMoreHH NUMBER,
                            MarriedCouple4HH NUMBER,
                            MarriedCouple5HH NUMBER,
                            MarriedCoupleNoneHH NUMBER,
                            PowerParityLess45000 NUMBER,
                            PowerParity45000_90000 NUMBER,
                            PowerParity90000_150000 NUMBER,
                            PowerParity45000_150000 NUMBER,
                            PowerParity150000_240000 NUMBER,
                            PowerParity240000_330000 NUMBER,
                            PowerParity150000_330000 NUMBER,
                            PowerParity330000_425000 NUMBER,
                            PowerParity425000_545000 NUMBER,
                            PowerParity330000_545000 NUMBER,
                            PowerParityAbove545000 NUMBER,
                            TotalPowerParity NUMBER,
                            CONSTRAINT fk_district_code_hh FOREIGN KEY (District_Code) REFERENCES Districts (District_Code)
                        )
                        """
                    ]

                    # Execute schema queries
                    for query in table_queries:
                        try:
                            cursor.execute(query)
                            print("Table created successfully.")
                        except cx_Oracle.DatabaseError as err:
                            print(f"Error creating table: {err}")

                # Commiting the DB changes
                connection.commit()

    except cx_Oracle.DatabaseError as err:
        print(f"Error connecting to MySQL: {err}")


# Call the function to create the schema
#rdbms_table_creation()

# %%
def load_data_to_oracle_db():
    # MongoDB connection
    mongo_collection = connect_mongo()

    # Oracle connection
    oracle_connection = connect_oracledb()
    oracle_cursor = oracle_connection.cursor()

    print('Able to connect with MongoDB and Oracle DB')

    def fetch_districts_from_mongodb():
        try:
            # Fetch data from MongoDB
            fetch_districts_data = list(
                mongo_collection.find({}, {'District_Code': 1, 'State_UT': 1, 'District_Name': 1,
                                           'Population': 1, '_id': 0}))
            return fetch_districts_data

        except Exception as e:
            print(f"An error occurred while fetching data from MongoDB: {e}")
            return None

    def insert_districts(cursor, districts):
        try:
            for district in districts:
                district_code = district.get('District_Code')
                state_ut = district.get('State_UT')
                district_name = district.get('District_Name')
                population = district.get('Population')

                cursor.execute("""
                    INSERT INTO DISTRICTS (DISTRICT_CODE, STATE_UT, DISTRICT_NAME, POPULATION)
                    VALUES (:1, :2, :3, :4)
                """, (district_code, state_ut, district_name, population))

            print("Districts inserted successfully.")

        except cx_Oracle.DatabaseError as err:
            print(f"Error inserting districts: {err}")

    def load_district_data():
        # Fetch districts data from MongoDB
        districts_data = fetch_districts_from_mongodb()

        if districts_data:
            # Insert districts data into Oracle DB
            insert_districts(oracle_cursor, districts_data)

            # Commit changes
            oracle_connection.commit()
        else:
            print("No data fetched from MongoDB.")

    def fetch_demographics_from_mongodb():
        try:
            # Fetch data from MongoDB
            demographics_data = list(mongo_collection.find({}, {
                'District_Code': 1, 'State_UT': 1, 'District_Name': 1, 'Population': 1,
                'Male': 1, 'Female': 1, 'Literate': 1, 'MaleLiterate': 1, 'FemaleLiterate': 1,
                'SC': 1, 'MaleSC': 1, 'FemaleSC': 1, 'ST': 1, 'MaleST': 1, 'FemaleST': 1,
                'BelowPrimaryEdu': 1, 'PrimaryEdu': 1, 'MiddleEdu': 1, 'SecondaryEdu': 1, 'HigherEdu': 1, 'GradEdu': 1,
                'OtherEdu': 1, 'LitEdu': 1, 'IllitEdu': 1, 'TotalEdu': 1,
                'Workers': 1, 'MaleWorkers': 1, 'FemaleWorkers': 1, 'MainWorkers': 1, 'MarginalWorkers': 1,
                'NonWorkers': 1, 'CultivatorWorkers': 1, 'AgrWorkers': 1, 'HHWorkers': 1, 'OtherWorkers': 1,
                'Hindus': 1, 'Muslims': 1, 'Christians': 1, 'Sikhs': 1, 'Buddhists': 1, 'Jains': 1,
                'Others_Religions': 1, 'RelNotStated': 1, 'Young_and_Adult': 1, 'Middle_Aged': 1,
                'Senior_Citizen': 1, 'Age_Not_Stated': 1, '_id': 0
            }))
            return demographics_data

        except Exception as e:
            print(f"An error occurred while fetching data from MongoDB: {e}")
            return None

    def insert_demographics(cursor, demographics):
        try:
            for demographic in demographics:
                district_code = demographic.get('District_Code')
                male = demographic.get('Male')
                female = demographic.get('Female')
                literate = demographic.get('Literate')
                male_literate = demographic.get('MaleLiterate')
                female_literate = demographic.get('FemaleLiterate')
                sc = demographic.get('SC')
                male_sc = demographic.get('MaleSC')
                female_sc = demographic.get('FemaleSC')
                st = demographic.get('ST')
                male_st = demographic.get('MaleST')
                female_st = demographic.get('FemaleST')
                belowprimaryedu = demographic.get('BelowPrimaryEdu')
                primaryedu = demographic.get('PrimaryEdu')
                middleedu = demographic.get('MiddleEdu')
                secondaryedu = demographic.get('SecondaryEdu')
                higheredu = demographic.get('HigherEdu')
                gradedu = demographic.get('GradEdu')
                otheredu = demographic.get('OtherEdu')
                litedu = demographic.get('LitEdu')
                illitedu = demographic.get('IllitEdu')
                totaledu = demographic.get('TotalEdu')
                workers = demographic.get('Workers')
                male_workers = demographic.get('MaleWorkers')
                female_workers = demographic.get('FemaleWorkers')
                main_workers = demographic.get('MainWorkers')
                marginal_workers = demographic.get('MarginalWorkers')
                non_workers = demographic.get('NonWorkers')
                cultivator_workers = demographic.get('CultivatorWorkers')
                agr_workers = demographic.get('AgrWorkers')
                hh_workers = demographic.get('HHWorkers')
                other_workers = demographic.get('OtherWorkers')
                hindus = demographic.get('Hindus')
                muslims = demographic.get('Muslims')
                christians = demographic.get('Christians')
                sikhs = demographic.get('Sikhs')
                buddhists = demographic.get('Buddhists')
                jains = demographic.get('Jains')
                others_religions = demographic.get('Others_Religions')
                rel_not_stated = demographic.get('RelNotStated')
                young_and_adult = demographic.get('Young_and_Adult')
                middle_aged = demographic.get('Middle_Aged')
                senior_citizen = demographic.get('Senior_Citizen')
                age_not_stated = demographic.get('Age_Not_Stated')

                cursor.execute("""
                            INSERT INTO demographics (DEMO_ID, District_Code, Male, Female, Literate, MaleLiterate, FemaleLiterate, SC, MaleSC, FemaleSC, ST, MaleST, FemaleST, BelowPrimaryEdu, PrimaryEdu, MiddleEdu, SecondaryEdu, HigherEdu, GradEdu, OtherEdu, LitEdu, IllitEdu, TotalEdu, Workers, MaleWorkers, FemaleWorkers, MainWorkers, MarginalWorkers, NonWorkers, CultivatorWorkers, AgrWorkers, HHWorkers, OtherWorkers, Hindus, Muslims, Christians, Sikhs, Buddhists, Jains, Others_Religions, RelNotStated, Young_and_Adult, Middle_Aged, Senior_Citizen, Age_Not_Stated)
                            VALUES (DEMO_SEQUENCE.NEXTVAL, :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21, :22, :23, :24, :25, :26, :27, :28, :29, :30, :31, :32, :33, :34, :35, :36, :37, :38, :39, :40, :41, :42, :43, :44)
                            """, (
                    district_code, male, female, literate, male_literate, female_literate, sc, male_sc, female_sc, st,
                    male_st,
                    female_st, belowprimaryedu, primaryedu, middleedu, secondaryedu, higheredu, gradedu, otheredu,
                    litedu, illitedu, totaledu, workers, male_workers, female_workers, main_workers, marginal_workers,
                    non_workers,
                    cultivator_workers, agr_workers, hh_workers, other_workers, hindus, muslims, christians, sikhs,
                    buddhists,
                    jains, others_religions, rel_not_stated, young_and_adult, middle_aged, senior_citizen,
                    age_not_stated))

            print("Demographics data inserted successfully.")

        except cx_Oracle.DatabaseError as err:
            print(f"Error inserting Demographics: {err}")

    def load_demographics_data():
        # Fetch Demographics data from MongoDB
        demographics_data = fetch_demographics_from_mongodb()

        if demographics_data:
            # Insert demographics data into Oracle DB
            insert_demographics(oracle_cursor, demographics_data)

            # Commit changes
            oracle_connection.commit()
        else:
            print("No data fetched from MongoDB.")

    def fetch_household_from_mongodb():
        try:
            # Fetch data from MongoDB
            household_data = list(mongo_collection.find({}, {
                'District_Code': 1, 'LPGHH': 1, 'ElecLightHH': 1, 'InternetHH': 1, 'ComputerHH': 1, 'RuralHH': 1,
                'UrbanHH': 1, 'TotalHH': 1, 'BicycleHH': 1, 'CarJeepVanHH': 1, 'RadioTransHH': 1,
                'ScooterMotorMopedHH': 1,
                'PhoneLandlineHH': 1, 'MobileOnlyHH': 1, 'TVCompLaptopHH': 1, 'TVHH': 1, 'PhoneHH': 1, 'PhoneBothHH': 1,
                'DilapHouseHH': 1, 'SepKitchenHH': 1, 'BathFacHH': 1, 'LatrineFacHH': 1, 'OwnedHH': 1, 'RentedHH': 1,
                'BathFacEnclosureHH': 1, 'OtherFuelHH': 1, 'PitLatrineHH': 1, 'OtherLatrineHH': 1,
                'NightSoilLatrineHH': 1,
                'FlushLatrineHH': 1, 'NoBathFacHH': 1, 'NoLatrineFacHH': 1, 'UncoveredWellWaterHH': 1,
                'HandpumpWaterHH': 1,
                'SpringWaterHH': 1, 'RiverCanalWaterHH': 1,
                'OtherWaterHH': 1, 'OtherWaterHH_River': 1, 'NearPremisesWaterHH': 1, 'WithinPremisesWaterHH': 1,
                'PondLakeWaterHH': 1,
                'TapWaterHH': 1, 'BoreholeWaterHH': 1, 'HHSize1Person': 1, 'HHSize2Persons': 1, 'HHSize1To2Persons': 1,
                'HHSize3Persons': 1, 'HHSize3To5Persons': 1, 'HHSize4Persons': 1, 'HHSize5Persons': 1,
                'HHSize6_8Persons': 1,
                'HHSize9AbovePersons': 1, 'AwayWaterSourceHH': 1, 'MarriedCouple1HH': 1, 'MarriedCouple2HH': 1,
                'MarriedCouple3HH': 1,
                'MarriedCouple3OrMoreHH': 1, 'MarriedCouple4HH': 1, 'MarriedCouple5HH': 1, 'MarriedCoupleNoneHH': 1,
                'PowerParityLess45000': 1,
                'PowerParity45000_90000': 1, 'PowerParity90000_150000': 1, 'PowerParity45000_150000': 1,
                'PowerParity150000_240000': 1,
                'PowerParity240000_330000': 1, 'PowerParity150000_330000': 1, 'PowerParity330000_425000': 1,
                'PowerParity425000_545000': 1,
                'PowerParity330000_545000': 1, 'PowerParityAbove545000': 1, 'TotalPowerParity': 1, '_id': 0
            }))
            return household_data

        except Exception as e:
            print(f"An error occurred while fetching data from MongoDB: {e}")
            return None

    def insert_household(cursor, households):
        try:
            for household in households:
                district_code = household.get('District_Code')
                lpghh = household.get('LPGHH')
                eleclighthh = household.get('ElecLightHH')
                internethh = household.get('InternetHH')
                computerhh = household.get('ComputerHH')
                ruralhh = household.get('RuralHH')
                urbanhh = household.get('UrbanHH')
                totalhh = household.get('TotalHH')
                bicyclehh = household.get('BicycleHH')
                carjeepvanhh = household.get('CarJeepVanHH')
                radiotranshh = household.get('RadioTransHH')
                scootermotormopedhh = household.get('ScooterMotorMopedHH')
                phonelandlinehh = household.get('PhoneLandlineHH')
                mobileonlyhh = household.get('MobileOnlyHH')
                tvcomplaptophh = household.get('TVCompLaptopHH')
                tvhh = household.get('TVHH')
                phonehh = household.get('PhoneHH')
                phonebothhh = household.get('PhoneBothHH')
                dilaphousehh = household.get('DilapHouseHH')
                sepkitchenhh = household.get('SepKitchenHH')
                bathfachh = household.get('BathFacHH')
                latrinefachh = household.get('LatrineFacHH')
                ownedhh = household.get('OwnedHH')
                rentedhh = household.get('RentedHH')
                bathfacenclosurehh = household.get('BathFacEnclosureHH')
                otherfuelhh = household.get('OtherFuelHH')
                pitlatrinehh = household.get('PitLatrineHH')
                otherlatrinehh = household.get('OtherLatrineHH')
                nightsoillatrinehh = household.get('NightSoilLatrineHH')
                flushlatrinehh = household.get('FlushLatrineHH')
                nobathfachh = household.get('NoBathFacHH')
                nolatrinefachh = household.get('NoLatrineFacHH')
                uncoveredwellwaterhh = household.get('UncoveredWellWaterHH')
                handpumpwaterhh = household.get('HandpumpWaterHH')
                springwaterhh = household.get('SpringWaterHH')
                rivercanalwaterhh = household.get('RiverCanalWaterHH')
                otherwaterhh = household.get('OtherWaterHH')
                otherwaterhh_river = household.get('OtherWaterHH_River')
                nearpremiseswaterhh = household.get('NearPremisesWaterHH')
                withinpremiseswaterhh = household.get('WithinPremisesWaterHH')
                pondlakewaterhh = household.get('PondLakeWaterHH')
                tapwaterhh = household.get('TapWaterHH')
                boreholewaterhh = household.get('BoreholeWaterHH')
                hhsize1person = household.get('HHSize1Person')
                hhsize2persons = household.get('HHSize2Persons')
                hhsize1to2persons = household.get('HHSize1To2Persons')
                hhsize3persons = household.get('HHSize3Persons')
                hhsize3to5persons = household.get('HHSize3To5Persons')
                hhsize4persons = household.get('HHSize4Persons')
                hhsize5persons = household.get('HHSize5Persons')
                hhsize6_8persons = household.get('HHSize6_8Persons')
                hhsize9abovepersons = household.get('HHSize9AbovePersons')
                awaywatersourcehh = household.get('AwayWaterSourceHH')
                marriedcouple1hh = household.get('MarriedCouple1HH')
                marriedcouple2hh = household.get('MarriedCouple2HH')
                marriedcouple3hh = household.get('MarriedCouple3HH')
                marriedcouple3ormorehh = household.get('MarriedCouple3OrMoreHH')
                marriedcouple4hh = household.get('MarriedCouple4HH')
                marriedcouple5hh = household.get('MarriedCouple5HH')
                marriedcouplenonehh = household.get('MarriedCoupleNoneHH')
                powerparityless45000 = household.get('PowerParityLess45000')
                powerparity45000_90000 = household.get('PowerParity45000_90000')
                powerparity90000_150000 = household.get('PowerParity90000_150000')
                powerparity45000_150000 = household.get('PowerParity45000_150000')
                powerparity150000_240000 = household.get('PowerParity150000_240000')
                powerparity240000_330000 = household.get('PowerParity240000_330000')
                powerparity150000_330000 = household.get('PowerParity150000_330000')
                powerparity330000_425000 = household.get('PowerParity330000_425000')
                powerparity425000_545000 = household.get('PowerParity425000_545000')
                powerparity330000_545000 = household.get('PowerParity330000_545000')
                powerparityabove545000 = household.get('PowerParityAbove545000')
                totalpowerparity = household.get('TotalPowerParity')

                cursor.execute("""
                            INSERT INTO Household (Household_ID, District_Code, LPGHH, ElecLightHH, InternetHH, ComputerHH, RuralHH, UrbanHH, TotalHH, BicycleHH, CarJeepVanHH, RadioTransHH, ScooterMotorMopedHH, PhoneLandlineHH, MobileOnlyHH, TVCompLaptopHH, TVHH, PhoneHH, PhoneBothHH, DilapHouseHH, SepKitchenHH, BathFacHH, LatrineFacHH, OwnedHH, RentedHH, BathFacEnclosureHH, OtherFuelHH, PitLatrineHH, OtherLatrineHH, NightSoilLatrineHH, FlushLatrineHH, 
                                                NoBathFacHH, NoLatrineFacHH, UncoveredWellWaterHH, HandpumpWaterHH, SpringWaterHH, RiverCanalWaterHH, OtherWaterHH, OtherWaterHH_River, NearPremisesWaterHH, WithinPremisesWaterHH, PondLakeWaterHH, 
                                                TapWaterHH, BoreholeWaterHH, HHSize1Person, HHSize2Persons, HHSize1To2Persons, HHSize3Persons, HHSize3To5Persons, HHSize4Persons, HHSize5Persons, HHSize6_8Persons, HHSize9AbovePersons, AwayWaterSourceHH, MarriedCouple1HH, MarriedCouple2HH, MarriedCouple3HH, MarriedCouple3OrMoreHH, MarriedCouple4HH, MarriedCouple5HH, MarriedCoupleNoneHH, PowerParityLess45000, PowerParity45000_90000, PowerParity90000_150000, PowerParity45000_150000, PowerParity150000_240000, PowerParity240000_330000, PowerParity150000_330000, PowerParity330000_425000, PowerParity425000_545000, PowerParity330000_545000, PowerParityAbove545000, TotalPowerParity)                             
                            VALUES (HH_SEQUENCE.NEXTVAL, :1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21, :22, :23, :24, :25, :26, :27, :28, :29, :30, :31, :32, :33, :34, :35, :36, :37, :38, :39, :40, :41, :42, :43, :44, :45, :46, :47, :48, :49, :50, :51, :52, :53, :54, :55, :56, :57, :58, :59, :60, :61, :62, :63, :64, :65, :66, :67, :68, :69, :70, :71, :72)
                            """, (
                    district_code, lpghh, eleclighthh, internethh, computerhh, ruralhh, urbanhh, totalhh, bicyclehh,
                    carjeepvanhh, radiotranshh, scootermotormopedhh, phonelandlinehh, mobileonlyhh, tvcomplaptophh,
                    tvhh,
                    phonehh, phonebothhh, dilaphousehh, sepkitchenhh, bathfachh, latrinefachh, ownedhh, rentedhh,
                    bathfacenclosurehh, otherfuelhh, pitlatrinehh, otherlatrinehh, nightsoillatrinehh, flushlatrinehh,
                    nobathfachh, nolatrinefachh, uncoveredwellwaterhh, handpumpwaterhh, springwaterhh,
                    rivercanalwaterhh,
                    otherwaterhh, otherwaterhh_river, nearpremiseswaterhh, withinpremiseswaterhh, pondlakewaterhh,
                    tapwaterhh,
                    boreholewaterhh, hhsize1person, hhsize2persons, hhsize1to2persons, hhsize3persons,
                    hhsize3to5persons,
                    hhsize4persons, hhsize5persons, hhsize6_8persons, hhsize9abovepersons, awaywatersourcehh,
                    marriedcouple1hh,
                    marriedcouple2hh, marriedcouple3hh, marriedcouple3ormorehh, marriedcouple4hh, marriedcouple5hh,
                    marriedcouplenonehh, powerparityless45000, powerparity45000_90000, powerparity90000_150000,
                    powerparity45000_150000, powerparity150000_240000, powerparity240000_330000,
                    powerparity150000_330000,
                    powerparity330000_425000, powerparity425000_545000, powerparity330000_545000,
                    powerparityabove545000,
                    totalpowerparity))

            print("Household data inserted successfully.")

        except cx_Oracle.DatabaseError as err:
            print(f"Error inserting Demographics: {err}")

    def load_household_data():
        # Fetch household data from MongoDB
        household_data = fetch_household_from_mongodb()

        if household_data:
            # Insert household data into Oracle DB
            insert_household(oracle_cursor, household_data)

            # Commit changes
            oracle_connection.commit()
        else:
            print("No data fetched from MongoDB.")

    load_district_data()
    load_demographics_data()
    load_household_data()


#load_data_to_oracle_db()

def oracle_tables_to_df():
    oracle_connection = connect_oracledb()
    oracle_cursor = oracle_connection.cursor()

    def fetch_data_to_dataframe(query, connection):
        try:
            # Execute the query
            oracle_cursor.execute(query)

            # Fetch all rows from the executed query
            rows = oracle_cursor.fetchall()

            # Get the column names from the cursor
            col_names = [col[0] for col in oracle_cursor.description]

            # Create a DataFrame from the fetched data
            df = pd.DataFrame(rows, columns=col_names)

            return df
        except cx_Oracle.DatabaseError as e:
            print(f"Error fetching data: {e}")
            return None

    districts_query = "SELECT * FROM Districts order by DISTRICT_CODE"
    demographics_query = "SELECT * FROM Demographics order by DISTRICT_CODE"
    household_query = "SELECT * FROM Household order by DISTRICT_CODE"

    # Load data into DataFrames
    districts_df = fetch_data_to_dataframe(districts_query, oracle_connection)
    demographics_df = fetch_data_to_dataframe(demographics_query, oracle_connection)
    household_df = fetch_data_to_dataframe(household_query, oracle_connection)

    # Close the cursor and connection
    oracle_cursor.close()
    oracle_connection.close()

    return districts_df, demographics_df, household_df


#oracle_tables_to_df()

# %%
def drop_mongodb_collection():
    try:
        mongo_connection = connect_mongo()
        mongo_connection.drop()
        print(f"Collection dropped successfully.")
    except Exception as e:
        print(f"An error occurred while dropping the MongoDB collection: {e}")


#drop_mongodb_collection()

# %%
# App Title
st.title("Census Data Analysis")

# Session State Initialization
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()
if 'df_updated' not in st.session_state:
    st.session_state.df_updated = pd.DataFrame()
if 'comparison' not in st.session_state:
    st.session_state.comparison = pd.DataFrame()
if 'districts_df' not in st.session_state:
    st.session_state.districts_df = pd.DataFrame()
if 'demographics_df' not in st.session_state:
    st.session_state.demographics_df = pd.DataFrame()
if 'household_df' not in st.session_state:
    st.session_state.household_df = pd.DataFrame()
if 'result_df' not in st.session_state:
    st.session_state.result_df = pd.DataFrame()

# Sidebar background color change
sidebar_style = """
    <style>
    [data-testid="stSidebar"] {
        background-color: #c2c2d6;
    }
    </style>
    """
st.markdown(sidebar_style, unsafe_allow_html=True)

# Sidebar for Actions
st.sidebar.header("Actions")

# Fetch Census Data
if st.sidebar.button("Fetch Census Data"):
    with st.spinner("Fetching data..."):
        st.session_state.df = fetch_data()
    st.success("Data fetched successfully!")
    st.balloons()

# Data Standardization
if st.sidebar.button("Data Standardization"):
    with st.spinner("Standardizing data..."):
        st.session_state.df = rename_columns(st.session_state.df)
        st.session_state.df = state_name_formatting(st.session_state.df)
        st.session_state.df_updated, st.session_state.comparison = null_value_percent_filling(st.session_state.df)
    st.success("Data standardized successfully!")

# Show Standardization Result
if st.sidebar.button("Show Standardization Result"):
    st.header("Standardization Result")
    st.write(st.session_state.comparison)

# Load Data to MongoDB
if st.sidebar.button("Load Census Data to MongoDB"):
    with st.spinner("Loading data to MongoDB..."):
        data_load_into_mongodb(st.session_state.df_updated)
    st.success("Data loaded successfully into MongoDB!")

# Load Data to Oracle DB
if st.sidebar.button("Load Data to Oracle DB"):
    with st.spinner("Loading data to Oracle DB..."):
        rdbms_table_creation()
        load_data_to_oracle_db()
        districts_df, demographics_df, household_df = oracle_tables_to_df()

        # Display data in Streamlit
        st.header("District wise data")
        st.dataframe(districts_df)

        st.header("Demographics wise data")
        st.dataframe(demographics_df)

        st.header("Household wise data")
        st.dataframe(household_df)
        drop_mongodb_collection()
    st.success("Data loaded successfully into Oracle DB!")


# Function to execute a query and return the result as a DataFrame
def run_query(query):
    connection = connect_oracledb()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    cursor.close()
    connection.close()
    return pd.DataFrame(result, columns=columns)


# Function to perform analysis based on selected question
def analysis(question):
    q1 = "1. What is the total population of each district?"
    q2 = "2. How many literate males and females are there in each district?"
    q3 = "3. What is the percentage of workers (both male and female) in each district?"
    q4 = "4. How many households have access to LPG or PNG as a cooking fuel in each district?"
    q5 = "5. What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?"
    q6 = "6. How many households have internet access in each district?"
    q7 = "7. What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?"
    q8 = "8. How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?"
    q9 = "9. What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?"
    q10 = "10. How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?"
    q11 = "11. What is the total number of households in each state?"
    q12 = "12. How many households have a latrine facility within the premises in each state?"
    q13 = "13. What is the average household size in each state?"
    q14 = "14. How many households are owned versus rented in each state?"
    q15 = "15. What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?"
    q16 = "16. How many households have access to drinking water sources near the premises in each state?"
    q17 = "17. What is the average household income distribution in each state based on the power parity categories?"
    q18 = "18. What is the percentage of married couples with different household sizes in each state?"
    q19 = "19. How many households fall below the poverty line in each state based on the power parity categories?"
    q20 = "20. What is the overall literacy rate (percentage of literate population) in each state?"

    queries = {
        q1: "select district_name, population from districts order by district_name",
        q2: "select disct.district_name, demo.maleliterate, demo.femaleliterate from districts disct left join demographics demo on disct.district_code = demo.district_code order by disct.district_name",
        q3: """SELECT 
                disct.district_name, 
                CASE 
                    WHEN demo.workers = 0 THEN 0 
                    ELSE ROUND((demo.maleworkers / demo.workers) * 100, 2) 
                END AS MaleWorkerPercentage,
                CASE 
                    WHEN demo.workers = 0 THEN 0 
                    ELSE ROUND((demo.femaleworkers / demo.workers) * 100, 2) 
                END AS FemaleWorkerPercentage
            FROM 
                districts disct
            LEFT JOIN 
                demographics demo
            ON 
                disct.district_code = demo.district_code
            order by disct.district_name""",
        q4: "select disct.district_name, hh.lpghh as HouseholdsWithLPGPNG from districts disct left join household hh on disct.district_code = hh.district_code order by disct.district_name",
        q5: """SELECT disct.district_name, 
                CASE 
                    WHEN disct.population = 0 THEN 0 
                    ELSE ROUND((demo.hindus / disct.population) * 100, 2) 
                END AS HindusPercentage,
                CASE 
                    WHEN disct.population = 0 THEN 0 
                    ELSE ROUND((demo.Muslims / disct.population) * 100, 2) 
                END AS MuslimsPercentage,
                CASE 
                    WHEN disct.population = 0 THEN 0 
                    ELSE ROUND((demo.Christians / disct.population) * 100, 2) 
                END AS ChristiansPercentage,
                CASE 
                    WHEN disct.population = 0 THEN 0 
                    ELSE ROUND((demo.Sikhs / disct.population) * 100, 2) 
                END AS SikhsPercentage,
                CASE 
                    WHEN disct.population = 0 THEN 0 
                    ELSE ROUND((demo.Buddhists / disct.population) * 100, 2) 
                END AS BuddhistsPercentage,
                CASE 
                    WHEN disct.population = 0 THEN 0 
                    ELSE ROUND((demo.Jains / disct.population) * 100, 2) 
                END AS JainsPercentage,
                CASE 
                    WHEN disct.population = 0 THEN 0 
                    ELSE ROUND((demo.Others_Religions / disct.population) * 100, 2) 
                END AS Others_ReligionsPercentage,
                CASE 
                    WHEN disct.population = 0 THEN 0 
                    ELSE ROUND((demo.RelNotStated / disct.population) * 100, 2) 
                END AS Religion_not_stated_Percentage
                FROM districts disct
                LEFT JOIN 
                demographics demo
                ON 
                disct.district_code = demo.district_code
                order by disct.district_name""",
        q6: "SELECT disct.district_name, hh.internethh from districts disct left join household hh on disct.district_code = hh.district_code order by disct.district_name",
        q7: """select disct.district_name, demo.BelowPrimaryEdu as Below_Primary_Education, demo.PrimaryEdu as Primary_Education, demo.MiddleEdu as Middle_Education, demo.SecondaryEdu as Secondary_Education,
                demo.HigherEdu as Higher_Education, demo.GradEdu as Graduate_Education, demo.otheredu as Other_Education 
                from districts disct 
                left join demographics demo 
                on disct.district_code = demo.district_code 
                order by disct.district_name""",
        q8: """SELECT disct.district_name, hh.bicyclehh as HH_with_Bicycle, hh.carjeepvanhh as HH_with_Car_Jeep_van, hh.SCOOTERMOTORMOPEDHH as HH_with_Scooter_Motor_Moped 
                from districts disct 
                left join household hh 
                on disct.district_code = hh.district_code 
                order by disct.district_name""",
        q9: """SELECT disct.district_name, hh.DilapHouseHH as HH_with_Dilapidated, hh.SepKitchenHH as HH_with_Seperate_Kitchen, hh.BathFacHH as HH_with_Bathroon_facility , hh.LatrineFacHH as HH_Latrin_Facility from districts disct left join household hh on disct.district_code = hh.district_code order by disct.district_name""",
        q10: """SELECT disct.district_name, hh.HHSize1Person as HH_with_1Person, hh.HHSize2Persons as HH_with_2Persons, hh.HHSize3Persons as HH_with_3Persons, hh.HHSize4Persons as HH_with_4Persons,
                hh.HHSize5Persons as HH_with_5Persons, hh.HHSize6_8Persons as HH_with_6_8Persons, hh.HHSize9AbovePersons as HH_with_9AbovePersons, hh.HHSize1To2Persons as HH_with_1To2Persons, hh.HHSize3To5Persons as HH_with_3To5Persons 
                from districts disct 
                left join household hh 
                on disct.district_code = hh.district_code 
                order by disct.district_name""",
        q11: """SELECT disct.state_ut, sum(hh.totalhh)
                from districts disct 
                left join household hh 
                on disct.district_code = hh.district_code 
                group by disct.state_ut
                order by disct.state_ut""",
        q12: """SELECT disct.state_ut, sum(hh.latrinefachh) as State_with_latrin_FC
                from districts disct 
                left join household hh 
                on disct.district_code = hh.district_code 
                group by disct.state_ut
                order by disct.state_ut""",
        q13: """SELECT 
                disct.state_ut,
                CASE 
                    WHEN SUM(hh.totalhh) = 0 THEN 0 
                    ELSE SUM(
                        hh.HHSize1Person * 1 + 
                        hh.HHSize2Persons * 2 + 
                        hh.HHSize1To2Persons * 1.5 + 
                        hh.HHSize3Persons * 3 + 
                        hh.HHSize3To5Persons * 4 + 
                        hh.HHSize4Persons * 4 + 
                        hh.HHSize5Persons * 5 + 
                        hh.HHSize6_8Persons * 7 + 
                        hh.HHSize9AbovePersons * 10 
                    ) / SUM(hh.totalhh) 
                END AS State_avg_HH_size
            FROM 
                districts disct 
            LEFT JOIN 
                household hh 
            ON 
                disct.district_code = hh.district_code 
            GROUP BY 
                disct.state_ut
            ORDER BY 
                disct.state_ut""",
        q14: """SELECT disct.state_ut, sum(hh.ownedhh) AS Owned_HH, sum(hh.rentedhh) AS Rented_HH
                from districts disct 
                left join household hh 
                on disct.district_code = hh.district_code 
                group by disct.state_ut
                order by disct.state_ut""",
        q15: """SELECT disct.state_ut, sum(hh.PitLatrineHH) AS Pit_latrine, sum(hh.FlushLatrineHH) AS Flush_pour_flush_latrine, sum(hh.NightSoilLatrineHH) AS Open_drain_latrine, sum(hh.OtherLatrineHH) AS Other_latrine
                from districts disct 
                left join household hh 
                on disct.district_code = hh.district_code 
                group by disct.state_ut
                order by disct.state_ut""",
        q16: """SELECT disct.state_ut, sum(hh.nearpremiseswaterhh) AS HH_Near_Water_Permises
                from districts disct 
                left join household hh 
                on disct.district_code = hh.district_code 
                group by disct.state_ut
                order by disct.state_ut""",
        q17: """SELECT disct.state_ut, round(avg(hh.PowerParityLess45000), 2), round(avg(hh.PowerParity45000_90000), 2), round(avg(hh.PowerParity90000_150000), 2), round(avg(hh.PowerParity45000_150000), 2), round(avg(hh.PowerParity150000_240000), 2), round(avg(hh.PowerParity240000_330000), 2), round(avg(hh.PowerParity150000_330000), 2), round(avg(hh.PowerParity330000_425000 ), 2), round(avg(hh.PowerParity425000_545000), 2), round(avg(hh.PowerParity330000_545000), 2), round(avg(hh.PowerParityAbove545000),2)
                from districts disct 
                left join household hh 
                on disct.district_code = hh.district_code 
                group by disct.state_ut
                order by disct.state_ut""",
        q18: """SELECT 
                disct.state_ut, 
                ROUND(
                    CASE 
                        WHEN SUM(hh.totalhh) = 0 THEN 0 
                        ELSE SUM(hh.MarriedCouple1HH) / SUM(hh.totalhh) * 100
                    END, 
                    2
                ) AS avg_MarriedCouple1HH,
                    ROUND(
                    CASE 
                        WHEN SUM(hh.totalhh) = 0 THEN 0 
                        ELSE SUM(hh.MarriedCouple2HH) / SUM(hh.totalhh) * 100
                    END, 
                    2
                ) AS avg_MarriedCouple2HH,
                    ROUND(
                    CASE 
                        WHEN SUM(hh.totalhh) = 0 THEN 0 
                        ELSE SUM(hh.MarriedCouple3HH) / SUM(hh.totalhh) * 100
                    END, 
                    2
                ) AS avg_MarriedCouple3HH,
                    ROUND(
                    CASE 
                        WHEN SUM(hh.totalhh) = 0 THEN 0 
                        ELSE SUM(hh.MarriedCouple3OrMoreHH) / SUM(hh.totalhh) * 100
                    END, 
                    2
                ) AS avg_MarriedCouple3OrMoreHH,
                    ROUND(
                    CASE 
                        WHEN SUM(hh.totalhh) = 0 THEN 0 
                        ELSE SUM(hh.MarriedCouple4HH) / SUM(hh.totalhh) * 100
                    END, 
                    2
                ) AS avg_MarriedCouple4HH,
                    ROUND(
                    CASE 
                        WHEN SUM(hh.totalhh) = 0 THEN 0 
                        ELSE SUM(hh.MarriedCouple5HH) / SUM(hh.totalhh) * 100
                    END, 
                    2
                ) AS avg_MarriedCouple5HH,
                    ROUND(
                    CASE 
                        WHEN SUM(hh.totalhh) = 0 THEN 0 
                        ELSE SUM(hh.MarriedCoupleNoneHH) / SUM(hh.totalhh) * 100
                    END, 
                    2
                ) AS avg_MarriedCoupleNoneHH
            FROM 
                districts disct 
            LEFT JOIN 
                household hh 
            ON 
                disct.district_code = hh.district_code 
            GROUP BY 
                disct.state_ut
            ORDER BY 
                disct.state_ut""",
        q19: """SELECT disct.state_ut, sum(hh.POWERPARITYLESS45000) as BelowPovertyLine
                from districts disct 
                left join household hh 
                on disct.district_code = hh.district_code 
                group by disct.state_ut
                order by disct.state_ut""",
        q20: """SELECT disct.state_ut, 
                ROUND(
                                    CASE 
                                        WHEN sum(disct.population) = 0 THEN 0 
                                        ELSE SUM(demo.litedu) / SUM(disct.population) * 100
                                    END, 
                                    2
                                ) AS avg_state_literate
                from districts disct 
                left join demographics demo
                on disct.district_code = demo.district_code 
                group by disct.state_ut
                order by disct.state_ut"""
    }

    query = queries.get(question, "")
    if query:
        try:
            st.session_state.result_df = run_query(query)
            st.write(st.session_state.result_df)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error('Invalid question selected.')


# SQL Analysis questions
questions = [
    "1. What is the total population of each district?",
    "2. How many literate males and females are there in each district?",
    "3. What is the percentage of workers (both male and female) in each district?",
    "4. How many households have access to LPG or PNG as a cooking fuel in each district?",
    "5. What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?",
    "6. How many households have internet access in each district?",
    "7. What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?",
    "8. How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?",
    "9. What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?",
    "10. How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?",
    "11. What is the total number of households in each state?",
    "12. How many households have a latrine facility within the premises in each state?",
    "13. What is the average household size in each state?",
    "14. How many households are owned versus rented in each state?",
    "15. What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?",
    "16. How many households have access to drinking water sources near the premises in each state?",
    "17. What is the average household income distribution in each state based on the power parity categories?",
    "18. What is the percentage of married couples with different household sizes in each state?",
    "19. How many households fall below the poverty line in each state based on the power parity categories?",
    "20. What is the overall literacy rate (percentage of literate population) in each state?"
]

question = st.sidebar.selectbox("Select Question", questions)
# Analyze Button
if st.sidebar.button("Analyze"):
    analysis_result = analysis(question)
    st.write(analysis_result)

# Display Data
st.header("Census Data")
if not st.session_state.df.empty:
    st.dataframe(st.session_state.df.head())
else:
    st.info("No data available. Please fetch the data.")

# Footer
st.markdown("---")
st.markdown("Census 11 report")

# Website background formatting
st.markdown(
    """
    <style>
    .main { 
        background-color: #e0e0eb; 
    }
    </style>
    """,
    unsafe_allow_html=True
)
