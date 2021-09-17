# WhoIs Forward and Reverse Lookup
## The Problem
The IPv4 landscape is very flexible and can shift from organization to organization without notice. When identifying IP Addresses associated with Federal Agencies there is a lot of movement as well as hidden IP assests that may be associated.

---

## The Solution
Obtain a database that can associate IP Address with an organization. This method will allow us to be flexible when identifying IP addresses associated with an organizaiton.

## Data Source
from https://github.com/cisagov/dotgov-data

## Reverse DNS Import Script


The script uses multiple processes (10) with each process running through 10,000 records each. In addition to the base fields, the following fields are added.

1. TLD - (Top Level Domain .gov)

2. **US domains only** - TLD1 - (TLD - Country Codes)

3. **In-Progress** - SubDomain - (Subdomain of organization)

4. Domain - (registered domain name of organization)

5. Postgres Database Schema

6. Federal Cabinets - Cabinet level agencies

7. Additional Information needed - Federal Agencies - Sub organizations below the cabinet level and also independent agencies (Acronymns are tracked)

8. rlookup table - Contains all of the reverse dns data from the Opendata Project

9. Government view - This view is designed to show .gov only data and used the indexes to speed up the search.
