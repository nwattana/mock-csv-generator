from faker import Faker
import pandas as pd
import os


def create_output_dir():
    # current working directory
    output_dir = os.getcwd() + "/output/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir


def create_csv(output_dir):
    # current working directory
    csv_file = output_dir + "data.csv"
    fake = Faker()
    csv_columns = ["name", "age", "street", "city", "state", "zip", "lng", "lat", "ip"]
    data = []
    for _ in range(10000):
        data.append(
            [
                fake.name(),
                fake.random_int(min=18, max=80, step=1),
                fake.street_address(),
                fake.city(),
                fake.state(),
                fake.zipcode(),
                fake.longitude(),
                fake.latitude(),
                fake.ipv4(),
            ]
        )
    df = pd.DataFrame(data, columns=csv_columns)
    df.to_csv(csv_file, index=False)
    print(f"CSV file {csv_file} created successfully.")


def create_xlsx(output_dir):
    xlsx_file = output_dir + "data.xlsx"
    fake = Faker()
    xlsx_columns = ["name", "age", "street", "city", "state", "zip", "lng", "lat", "ip"]
    data = []
    for _ in range(10000):
        data.append(
            [
                fake.name(),
                fake.random_int(min=18, max=80, step=1),
                fake.street_address(),
                fake.city(),
                fake.state(),
                fake.zipcode(),
                fake.longitude(),
                fake.latitude(),
                fake.ipv4(),
            ]
        )
    df = pd.DataFrame(data, columns=xlsx_columns)
    df.to_excel(xlsx_file, index=False)
    print(f"XLSX file {xlsx_file} created successfully.")


def run():
    output_dir = create_output_dir()
    create_csv(output_dir)
    create_xlsx(output_dir)

if __name__ == "__main__":
    run()
