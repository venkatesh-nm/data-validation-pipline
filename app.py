import pandas as pd
import datetime

log_file = 'validation_log.txt'

def write_message(message):
    with open(log_file, 'a') as f:
        f.write(f'{datetime.datetime.now()} - {message}\n')

def validate_data(file_path):
    try:
        df = pd.read_csv(file_path)
        write_message('Data loaded successfully')

        errors = []

        if df.isnull().values.any():
            missing_data = df[df.isnull().any(axis=1)]
            errors.append(f'Missing values found:\n{missing_data}')

        if not df['age'].apply(lambda x: str(x).isdigit()).all():
            invalid_age_data - df[~df['age'].apply(lambda x: str(x).isdigit())]
            errors.append(f'Invalid age values found:\n{invalid_age_data}')


        if errors:
            for error in errors:
                write_message(error)
            write_message('Data validation failed.')
        else:
            write_message('Data Validation passes')

    except Exception as e:
        write_message(f'Data validation failed with error: {e}')


if __name__ == "__main__":
    csv_file_path = 'data.csv'
    validate_data(csv_file_path)

        
