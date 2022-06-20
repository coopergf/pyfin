# pyfin
### financial calculation experiments

This project is purely for experimentation and cannot be used to accurately calculate finances.

This project is in development.

### loan_repayment_schedule features / suggestions
* make each payment holiday period (month) be configurable to allow extension
* make each payment holiday period (month) be configurable to allow interest to be accrued
* allow for different rates / periods other than annual / twelve

### run example
```bash
python example_repayment_schedule.py | jq
```

### run api example
```bash
python example_restapi.py
```

### rest example
```bash
http://localhost:5000/repayment/schedule?present_value=25000&future_value=5000&rate=5.56&number_of_payments=24&payment_holiday=2,3,4&accrue_interest=true&extended=false
```

