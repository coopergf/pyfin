# pyfin
### financial calculation experiments

This project is purely for experimentation and cannot be used to accurately calculate finances.

This project is in development.

### loan_repayment_schedule features / suggestions
* make each payment holiday period (month) be configurable to allow extension
* make each payment holiday period (month) be configurable to allow interest to be accrued
* allow for different rates / periods other than annual / twelve

### rest example
```bash
http://localhost:5000/repayment/schedule?pv=25000&rate=5.86&fv=8500&nper=24&payment_holiday=2,3,4&extended=false&accrue_interest=false
```