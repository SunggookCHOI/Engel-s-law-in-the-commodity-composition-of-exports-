# Engel-s-law-in-the-commodity-composition-of-exports-
Source code for investigating the international trade. (Data preprocessing and draw figures)

<h2>Abstract</h2><br>
Different shares of distinct commodity sectors in production, trade, and consumption illustrate how resources and capital are allocated and invested. Economic progress has been claimed to change the share distribution in a universal manner as exempliﬁed by the Engel’s law for the household expenditure and the shift from primary to manufacturing and service sector in the three sector model. Searching for large-scale quantitative evidence of such correlation, we analyze the gross-domestic product (GDP) and international trade data based on the standard international trade classiﬁcation (SITC) in the period 1962 to 2000. Just three categories, among ten in the SITC, are found to have their export shares signiﬁcantly correlated with the GDP over countries and time; The machinery category has positive and food and crude materials have negative correlations. The export shares of commodity categories of a country are related to its GDP by a power-law with the exponents characterizing the GDP-elasticity of their export shares. The distance between the export portfolios of each pair of countries is measured to obtain several clusters of countries sharing similar portfolios in 1962 and 2000. We show that the countries whose GDP is increased signiﬁcantly in the period are likely to transit to the clusters displaying large share of the machinery category.<br>

<h2>Raw data</h2><br>

<b>1. rgdp_DSL.ver1.txt contains selected columns of the table in  pwt_v61.asc, included in the supplementary material of Ref. [35].</b>

col1: country code <br>
col2: country name (abbr.)<br>
col3: year<br>
col4: real GDP (constant million US dollars from year 1996, not current US dollars)<br>
col5: ratio of GDP in the constant yr-1996 US dollars to that in the current US dollars, 
  needed for compensating inflation<br>


<b>2. Export_from_wtf.txt contains selected data from Ref. [34].</b><br>

col1: year<br>
col2: country code <br>
col3: country name <br>
col4: product code(SITC-4)<br>
col5: trade amounts
