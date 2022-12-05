import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

main_ds = pd.read_csv("dataset.csv")

del main_ds["SCHOOL_ID"]
del main_ds["SCHOOL_TYPE"]
del main_ds["SPORT_CODE"]

main_ds = main_ds[main_ds.NCAA_DIVISION != 2]
main_ds = main_ds[main_ds.NCAA_DIVISION != 3]

df_with_na = main_ds.replace(-99, np.nan)

clean_df = df_with_na.dropna()

conference_eligibility_2014 = df_with_na.groupby('NCAA_CONFERENCE').mean()['2014_ELIGIBILITY']

by_conf = df_with_na.groupby('NCAA_CONFERENCE').mean()

by_sport = df_with_na.groupby('SPORT_NAME').mean()

by_school = df_with_na.groupby('SCHOOL_NAME').mean()

by_gender = by_sport.reset_index(level=0)

top_10_APR_by_school = by_school.sort_values(by = 'FOURYEAR_SCORE', ascending=False)[:10]
top_10_APR_by_school = top_10_APR_by_school.reset_index(level=0)


bottom_10_APR = by_school.sort_values(by = 'FOURYEAR_SCORE')[:10]
bottom_10_APR = bottom_10_APR.reset_index(level=0)

top_bottom_10 = pd.concat([top_10_APR_by_school, bottom_10_APR])

top_bottom_10['APR Rank'] = top_bottom_10['FOURYEAR_SCORE'] > 960

top_bottom_10 = top_bottom_10.replace(False, "Top 10 Piores Instituições")
top_bottom_10 = top_bottom_10.replace(True, "Top 10 Melhores Instituições")

top_bottom_10 = top_bottom_10.rename(index=str, columns={"2014_SCORE": "Pontuação APR - 2014",
                                                   "2004_SCORE": "Pontuação APR - 2004",
                                                   "FOURYEAR_ELIGIBILITY":
                                                       "Porcentagem de elegibilidade de 4 anos"})

sns.set()
sns.relplot(x="Pontuação APR - 2004", y="Pontuação APR - 2014", hue="APR Rank", size=
            "Porcentagem de elegibilidade de 4 anos",
            data=top_bottom_10)
plt.ylim(900, None)
plt.xlim(900, None)

plt.title("Progressão das pontuações APR no atletismo da Divisão 1 da NCAA")    
plt.savefig("Graph_1.png")
  
new_data = top_10_APR_by_school[['SCHOOL_NAME',
        '2014_SCORE', 
        '2013_SCORE', 
        '2012_SCORE', 
        '2011_SCORE', 
       '2010_SCORE', 
        '2009_SCORE', 
       '2008_SCORE', 
        '2007_SCORE', 
        '2006_SCORE', 
       '2005_SCORE',
       '2004_SCORE', ]]

new_top10 = pd.melt(new_data, id_vars=["SCHOOL_NAME"], 
                  var_name="Ano", value_name="Pontuação APR")

new_top10['Ano'] = new_top10['Ano'].apply(lambda yr: int(yr.replace('_SCORE','')))

new_bottom10 = bottom_10_APR[['SCHOOL_NAME',
        '2014_SCORE', 
        '2013_SCORE', 
        '2012_SCORE', 
        '2011_SCORE', 
       '2010_SCORE', 
        '2009_SCORE', 
       '2008_SCORE', 
        '2007_SCORE', 
        '2006_SCORE', 
       '2005_SCORE',
       '2004_SCORE']]

new_bottom10 = pd.melt(new_bottom10, id_vars=["SCHOOL_NAME"], 
                  var_name="Ano", value_name="Pontuação APR")

new_bottom10['Ano'] = new_bottom10['Ano'].apply(lambda yr: int(yr.replace('_SCORE','')))

new_top_bottom = pd.concat([new_bottom10, new_top10])

new_top_bottom['Piores ou Melhores'] = new_top_bottom['Pontuação APR']

new_top_bottom['Piores ou Melhores'].values[new_top_bottom['Piores ou Melhores'] < 981] = 0

new_top_bottom['Piores ou Melhores'].values[new_top_bottom['Piores ou Melhores'] > 981] = 1

new_top_bottom = new_top_bottom.replace(0, "Top 10 Piores Instituições")
new_top_bottom = new_top_bottom.replace(1, "Top 10 Melhores Instituições")

sns.relplot(x="Ano", y="Pontuação APR",
            hue="SCHOOL_NAME", col="Piores ou Melhores",
            facet_kws=dict(sharex=False),
            kind="line", legend="full", data=new_top_bottom);

plt.savefig("Graph_2.png")

power_5 = {"Big Ten Conference", "Atlantic Coast Conference", "Pac-12 Conference", 
           "Big 12 Conference", "Southeastern Conference", "The Ivy League"}

p5_academics = by_conf[by_conf.index.isin(power_5)]

p5_academics = p5_academics.reset_index(level=0)

new_p5 = p5_academics[['NCAA_CONFERENCE',
        '2014_SCORE', 
        '2013_SCORE', 
        '2012_SCORE', 
        '2011_SCORE', 
       '2010_SCORE', 
        '2009_SCORE', 
       '2008_SCORE', 
        '2007_SCORE', 
        '2006_SCORE', 
       '2005_SCORE',
       '2004_SCORE', ]]

new_p5 = pd.melt(new_p5, id_vars=["NCAA_CONFERENCE"], 
                  var_name="Ano", value_name="Pontuação APR")

new_p5['Ano'] = new_p5['Ano'].apply(lambda yr: int(yr.replace('_SCORE','')))

new_p5 = new_p5.rename(index=str, columns={'NCAA_CONFERENCE':'Conferência NCAA'})

sns.relplot(x="Ano", y="Pontuação APR",
            hue="Conferência NCAA",
            facet_kws=dict(sharex=False),
            kind="line", legend="full", data=new_p5);

plt.title("Conferências Power 5 e The Ivy League \n Progressão da pontuação APR\n")
plt.savefig("Graph_3.png")

exdf = clean_df[clean_df['NCAA_CONFERENCE'].str.match('Southeastern')]

exdf1 = clean_df[clean_df['NCAA_CONFERENCE'].str.match('Big Ten')]

exdf2 = clean_df[clean_df['NCAA_CONFERENCE'].str.match('Big 12')]

exdf3 = clean_df[clean_df['NCAA_CONFERENCE'].str.match('Pac-12')]

exdf4 = clean_df[clean_df['NCAA_CONFERENCE'].str.match('Atlantic Coast')]

exdf5 = clean_df[clean_df['NCAA_CONFERENCE'].str.match('The Ivy League')]

power_5_conferences = pd.concat([exdf, exdf1, exdf2, exdf3, exdf4, exdf5])

power_5_conferences = power_5_conferences.rename(index=str, columns={"FOURYEAR_SCORE": "Pontuação APR ao longo de 4 anos",
                                                   "NCAA_CONFERENCE": "Conferência NCAA"})
  
sns.catplot(x="Pontuação APR ao longo de 4 anos", y="Conferência NCAA",height=3.5, 
            aspect=1.5, kind="box", legend=False, data=power_5_conferences)
plt.title("Conferências Power 5 e The Ivy League \n Pontuação APR ao longo de 4 anos\n")
plt.savefig("Graph_4.png")
