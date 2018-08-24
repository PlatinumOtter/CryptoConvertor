# CryptoConvertor

This application provides a means of converting different types of cryptocurrencies on different exchanges as well as a generic web front end.

## API

The API is used to query a SQL database backend that contains the different rates used by different exchanges. The queries are simply structured like the following example.

`Insert example query here`

## Database & Backend

The database is a simple SQL database that is used to store a table for each individual exchange. Currently supported exchanges are INSERT SUPPORT HERE.

Everything in the databases is referenced back to bitcoin as it is consistently used as a point of reference for exchange rates for all of the alternative coins.

The back end application populates the Database with updates from the exchanges at regular intervals.

##  User Interface

The user-interface provided is a bare bones use of the API to provide quick load times and speed of use for power users.