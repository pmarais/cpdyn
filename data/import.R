library('httr')
library('lubridate')
library('dplyr')
setwd('~/workspace_pm/013_cpdyn/data/')

## Load the CSVs
df.cl <- read.csv('./Client.csv')
df.ac <- read.csv('./Account.csv')
df.tr <- read.csv('./Transaction.csv')

## Fix the Dates
df.ac$DateOpened <- gsub(" UTC$", "", parse_date_time(df.ac$DateOpened, 'd-m-y', truncated = 1))
df.tr$Date <- gsub(" UTC$", "", parse_date_time(df.tr$Date, 'd-m-y', truncated = 1))

######################
## Creating clients ##
######################
for (i in 1:nrow(df.cl)) {
  # print(df.cl[i,])
  rowlist = list(
    cl_name = df.cl$Name[i],
    cl_surname = df.cl$Surname[i],
    cl_pwd = df.cl$Password[i],
    cl_id = df.cl$IDNumber[i]
  )
  # print(rowlist)
  POST('http://localhost:8000/api/clients/', body = rowlist)
}

######################
## Creating clients ##
######################
for (i in 1:nrow(df.ac)) {
  # print(df.cl[i,])
  rowlist = list(
    acc_id = df.ac$AccountID[i] %>% as.integer(),
    acc_number = df.ac$AccountNumber[i] %>% as.integer(),
    acc_type = df.ac$AccountType[i] %>% as.character(),
    acc_opened = df.ac$DateOpened[i] %>% as.character(),
    acc_client = df.ac$ClientID[i] %>% as.integer()
  )
  print(rowlist)
  POST('http://localhost:8000/api/accounts/', body = rowlist)
}

for (i in 1:nrow(df.tr)) {
  # print(df.cl[i,])
  rowlist = list(
    tr_id = df.tr$TransactionID[i] %>% as.integer(),
    tr_amount = df.tr$Amount[i] %>% as.integer(),
    tr_date = df.tr$Date[i] %>% as.character(),
    tr_account = df.tr$AccountID[i] %>% as.integer()
  )
  print(rowlist)
  POST('http://localhost:8000/api/transactions/', body = rowlist)
}
