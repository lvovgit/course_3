from utils import get_data


def main():
    OPERATIONS_URL = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1675879263948&signature=J5h_0G2DVtgN5uXzvVpgxNf8ZTsSlvNTq9-rWdMJtuQ&downloadName=operations.json"
    FILTERED_EMPTY_FROM = True
    data, info = get_data(OPERATIONS_URL)
    if not data:
        exit(info)
    else:
        print(info)

    data = get_filtered_data(data, filtered_empty_from=FILTERED_EMPTY_FROM)
if __name__ == "__main__":
    main()