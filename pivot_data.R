library("tidyverse")

data = read.csv('ml_ranks_sorted.csv')

data %>%
  pivot_longer(cols=c("avgOrderIn","stdOrderIn","first30Out",
                      "medPerSec","stdTimeIn","first30In",
                      "maxPerSec","last30Out","medConc",
                      "per100Out","stdConc","avgOrderOut",
                      "maxConc","minPerSec","avgTimeOut",
                      "maxTimeIn","per100In","stdPerSec",
                      "avgConc","per75TimeOut","per75Total",
                      "perIn","stdTimeTotal","sumNumPack",
                      "sumTimeStats","avgAltPerSec","avgPerSec",
                      "per25Total","sumAltConc","avgAltConc",
                      "per100Total","per25In","per50In",
                      "per50Out","per50Total","per75In",
                      "per75TimeIn","per75TimeTotal","sumInterTimeStats",
                      "avgTimeTotal","maxTimeOut","packCountIn","per25Out",
                      "per75Out","perOut","stdTimeOut","maxTimeTotal",
                      "packCountTotal","sumAltPerSec","avgTimeIn",
                      "last30In","packCountOut","stdOrderOut"),
               names_to="Feature_Name", values_to="Median_Accuracy") %>%
  write.csv('ml_ranks_cleaned.csv', row.names = FALSE)