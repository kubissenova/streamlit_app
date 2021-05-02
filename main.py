import streamlit as st
import pandas as pd
import base64
import altair as alt
import matplotlib.pyplot as plt

dataset = st.sidebar.selectbox('Select dataset', ('Birth statistic', 'Population statistic'))

#user can choose ine of this dataset and chage it
#we have 2 dataset
#1 about birth and 2 about population

def get_dataset(name):
    #we made function to 2 dataset with if/else
    if name == 'Birth statistic':
        st.title('Birth statistic')

        st.markdown("""
        This app performs simple birth stats data!
        * **Python libraries:** pandas, streamlit
        * Data shows number of birth of 2 genders in exact time.
        """)

        df = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv')

        df = df.drop(
            labels=[62, 63, 126, 127, 190, 191, 254, 255, 318, 319, 382, 383, 446, 447, 510, 511, 574, 575, 638, 639, 702, 703, 766, 767,
                    830, 831, 894, 895, 958, 959, 1022, 1023, 1086, 1087, 1150, 1151, 1214, 1215, 1278, 1279, 1342, 1343, 1406, 1407, 1470,
                    1471, 1534, 1535, 1598, 1599, 1659, 1660, 1723, 1724, 1787, 1788, 1851, 1852, 1914, 1915, 1978, 1979, 2042, 2043, 2106,
                    2107, 2170, 2171, 2234, 2235, 2298, 2299, 2362, 2363, 2424, 2425, 2488, 2489, 2552, 2553, 2616, 2617, 2679, 2680, 2743,
                    2744, 2807, 2808, 2871, 2872, 2935, 2936, 2999, 3000, 3063, 3064, 3127, 3128, 3187, 3188, 3251, 3252, 3314, 3315, 3378,
                    3379, 3442, 3443, 3506, 3507, 3570, 3571, 3634, 3635, 3698, 3699, 3761, 3762, 3825, 3826, 3889, 3890, 3951, 3952, 4015,
                    4016, 4079, 4080, 4143, 4144, 4207, 4208, 4271, 4272, 4335, 4336, 4399, 4400, 4463, 4464, 4527, 4528, 4591, 4592, 4655,
                    4656, 4716, 4717, 4780, 4781, 4844, 4845, 4908, 4909, 4972, 4973, 5036, 5037, 5100, 5101, 5164, 5165, 5228, 5291, 5354,
                    5355, 5418, 5419, 5479, 5480, 5543, 5544, 5606, 5607, 5670, 5671, 5733, 5734, 5797, 5798, 5861, 5862, 5924, 5925, 5988,
                    5989, 6052, 6115, 6116, 6179, 6239, 6240, 6303, 6304, 6428, 6428, 6429, 6492, 6493, 6556, 6557, 6620, 6621, 6684, 6685,
                    6748, 6749, 6812, 6813, 6876, 6877, 7002, 7127, 7128, 7191, 7192, 7254, 7255, 7318, 7381, 7382, 7445, 7446, 7509, 7510,
                    7573, 7574, 7637, 7638, 7757, 7758, 7821, 7822, 7883, 7946, 8007, 8070, 8133, 8134, 8195, 8196, 8259, 8320, 8321, 8384,
                    8385, 8506, 8569, 8570, 8631, 8632, 8755, 8756, 8819, 8942, 8943, 9006, 9007, 9068, 9069, 9132, 9195, 9196, 9253, 9254,
                    9439, 9500, 9501, 9564, 9627, 9688, 9751, 9752, 9813, 9814, 9877, 9940, 9997, 9998, 10061, 10062, 10123, 10124, 10247,
                    10310, 10311, 10374, 10375, 10436, 10499, 10500, 10561, 10562, 10625, 10688, 10689, 10746, 10747, 10810, 10811, 10872,
                    10873, 10936, 10997, 10998, 11061, 11062, 11125, 11126, 11187, 11250, 11311, 11374, 11437, 11438, 11497, 11560, 11621,
                    11622, 11685, 11746, 11747, 11810, 11873, 11934, 12057, 12058, 12121, 12184, 12185, 12242, 12243, 12366, 12613, 12796,
                    12977, 12978, 13285, 13408, 13531, 13594, 13713, 13776, 13837, 14510, 14511, 14572, 14635, 14696, 14697, 14944], axis=0)
        df = df.dropna()
        df = df.reset_index(drop=True)
        #first of all, we found good dataset, but it had defects
        #for example, in dataset was 99th day, using their index, we delete it
        #and using dropna() function we delete none elements
        #reset function helps to reset index

        df1 = pd.read_csv(r"C:\Users\admin\Desktop\birth.csv")
        #then save new csv and worked with

        st.sidebar.header('User Input Features')

        sorted_year = sorted(df1.year.unique())
        selected_year = st.sidebar.multiselect('Year', sorted_year, sorted_year)

        gender = ['F', 'M']
        selected_gender = st.sidebar.multiselect('Gender', gender, gender)

        sorted_day = sorted(df1.day.unique())
        selected_day = st.sidebar.multiselect('Day', sorted_day, sorted_day)

        sorted_month = sorted(df1.month.unique())
        selected_month = st.sidebar.multiselect('Month', sorted_month, sorted_month)
        #unique elements that do not repeat

        df_selected_team = df1[(df1.day.isin(selected_day)) & (df1.gender.isin(selected_gender)) & (df1.year.isin(selected_year)) & (df1.month.isin(selected_month))]
        st.header('Birth stats of years')
        st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
        st.dataframe(df_selected_team)

        def filedownload(df):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="birth.csv">Download CSV File</a>'
            return href
        #function to download output

        st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)

        if st.button('Show Plots'):
            fig, ax = plt.subplots()
            ax.fill_between(df_selected_team.year, df_selected_team.births, color='blue', alpha=0.3)
            ax.plot(df_selected_team.year, df_selected_team.births, color='blue', alpha=0.8)
            st.pyplot(fig)

            p = alt.Chart(df_selected_team).mark_bar().encode(x='gender', y='births')
            p = p.properties(width=alt.Step(80))
            st.write(p)
            #we present 2 graphics
            #first is ratio of birth and year
            #2 compare two genders

    else:
        st.title('Population statistic')

        st.markdown("""
                This app performs simple population stats data of 2020 year!
                * **Python libraries:** pandas, streamlit
                """)
        data = pd.read_csv(r"C:\Users\admin\Desktop\population_by_country_2020.csv")
        st.sidebar.header('User Input Features')
        #next dataset about population

        sorted_country = sorted(data.Country.unique())
        selected_country = st.sidebar.multiselect('Country', sorted_country, sorted_country)

        data_selected_team = data[(data.Country.isin(selected_country))]

        st.header('Population Stats of 2020s')
        st.write('Data Dimension: ' + str(data_selected_team.shape[0]) + ' rows and ' + str(data_selected_team.shape[1]) + ' columns.')
        st.dataframe(data_selected_team)

        def filedownload(df):
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="population.csv">Download CSV File</a>'
            return href

        st.markdown(filedownload(data_selected_team), unsafe_allow_html=True)

        if st.button('Show Plots'):
            fig, ax = plt.subplots()
            ax.fill_between(data_selected_team.Country, data_selected_team.Population, color='skyblue', alpha=0.3)
            ax.plot(data_selected_team.Country, data_selected_team.Population, color='skyblue', alpha=0.8)
            st.pyplot(fig)
            #this plot shows ratio of country and population of this country

get_dataset(dataset)


