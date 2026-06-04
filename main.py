saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    try:
        choice = int(input("""
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình
================================================================
Mời bạn nhập lựa chọn: """))

        if choice < 1 or choice > 7:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
            continue

        match choice:
            case 1:
                if len(saving_accounts) == 0:
                    print("Danh sách sổ tiết kiệm hiện đang trống")
                    continue

                print("\nDanh sách sổ tiết kiệm:")

                for position, account in enumerate(saving_accounts, start=1):
                    print(
                        f"{position}. "
                        f"Mã sổ: {account['account_id']} | "
                        f"Khách hàng: {account['customer_name']} | "
                        f"Số tiền gửi: {account['balance']} | "
                        f"Kỳ hạn: {account['term_months']} tháng | "
                        f"Lãi suất: {account['interest_rate']}%/năm | "
                        f"Trạng thái: {account['status']}"
                    )

            case 2:
                new_account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()
                is_duplicate = False

                for account in saving_accounts:
                    if account["account_id"] == new_account_id:
                        is_duplicate = True
                        break

                if is_duplicate:
                    print("Mã sổ tiết kiệm bị trùng")
                    continue

                new_customer_name = input("Nhập tên khách hàng: ").strip()

                if not new_customer_name:
                    print("Tên khách hàng không được để trống")
                    continue

                while True:
                    try:
                        new_balance = int(input("Nhập số tiền gửi: "))

                        if new_balance <= 0:
                            print("Số tiền gửi phải là số nguyên dương")
                            continue

                        break

                    except ValueError:
                        print("Số tiền gửi phải là số nguyên dương")

                while True:
                    try:
                        new_term_months = int(input("Nhập kỳ hạn gửi theo tháng: "))

                        if new_term_months <= 0:
                            print("Kỳ hạn gửi phải là số nguyên dương")
                            continue

                        break

                    except ValueError:
                        print("Kỳ hạn gửi phải là số nguyên dương")

                while True:
                    try:
                        new_interest_rate = float(input("Nhập lãi suất năm: "))

                        if new_interest_rate <= 0:
                            print("Lãi suất năm phải lớn hơn 0")
                            continue

                        break

                    except ValueError:
                        print("Lãi suất năm phải lớn hơn 0")

                new_account = {
                    "account_id": new_account_id,
                    "customer_name": new_customer_name,
                    "balance": new_balance,
                    "term_months": new_term_months,
                    "interest_rate": new_interest_rate,
                    "status": "active"
                }

                saving_accounts.append(new_account)

                print("Mở sổ tiết kiệm mới thành công!")

            case 3:
                edit_account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
                is_found = False

                for account in saving_accounts:
                    if account["account_id"] == edit_account_id:
                        is_found = True

                        if account["status"] != "active":
                            print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                            break

                        new_customer_name = input("Nhập tên khách hàng mới: ").strip()

                        if not new_customer_name:
                            print("Tên khách hàng mới không được để trống")
                            break

                        while True:
                            try:
                                new_balance = int(input("Nhập số tiền gửi mới: "))

                                if new_balance <= 0:
                                    print("Số tiền gửi mới phải là số nguyên dương")
                                    continue

                                break

                            except ValueError:
                                print("Số tiền gửi mới phải là số nguyên dương")

                        while True:
                            try:
                                new_term_months = int(input("Nhập kỳ hạn mới theo tháng: "))

                                if new_term_months <= 0:
                                    print("Kỳ hạn mới phải là số nguyên dương")
                                    continue

                                break

                            except ValueError:
                                print("Kỳ hạn mới phải là số nguyên dương")

                        while True:
                            try:
                                new_interest_rate = float(input("Nhập lãi suất năm mới: "))

                                if new_interest_rate <= 0:
                                    print("Lãi suất năm mới phải lớn hơn 0")
                                    continue

                                break

                            except ValueError:
                                print("Lãi suất năm mới phải lớn hơn 0")

                        account["customer_name"] = new_customer_name
                        account["balance"] = new_balance
                        account["term_months"] = new_term_months
                        account["interest_rate"] = new_interest_rate

                        print("Cập nhật thông tin sổ tiết kiệm thành công!")
                        break

                if not is_found:
                    print("Không tìm thấy mã sổ tiết kiệm!")

            case 4:
                
                delete_saving_account_id = input("Mời bạn nhập vào mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
                is_found = False
                
                for account in saving_accounts:
                    
                    if account["account_id"] == delete_saving_account_id:
                        account["status"] = "closed"
                        print(f"Đã tất toán sổ tiết kiệm {delete_saving_account_id}")
                        is_found = True
                        
                
                if not is_found:
                    print(f"Không tìm thấy sp id {delete_saving_account_id}")
                

            case 5:
                # *** Chức năng 5: Tính lãi dự kiến khi đến hạn
                cal_interest_rate_id = input("Mời bạn nhập vào mã sổ tiết kiệm cần tính lãi: ").strip().upper()
                is_found = False
                interest_money = 0
                total_moeny = 0
                                
                for account in saving_accounts:
                    if account["account_id"] == cal_interest_rate_id and account["status"] == "active":
                        # tính tiền lãi
                        interest_money = account["balance"] * account["interest_rate"] / 100 * account["term_months"] / 12
                        
                        # tổng tiền dự kiến nhận được
                        total_moeny = account["balance"] + interest_money
                        is_found = True
                        
                if not is_found:
                    print("Không tìm thấy")
                    continue
                print(f"Tiền lãi dự kiến: {interest_money:,}VND")
                print(f"Tổng tiền nhận được: {total_moeny:,}VND")
                
                  
                
            case 6:
                check_account_id = input(
                    "Nhập mã sổ tiết kiệm cần kiểm tra: "
                ).strip().upper()

                is_found = False

                for account in saving_accounts:
                    if account["account_id"] == check_account_id:
                        is_found = True

                        if account["status"] != "active":
                            print("Chỉ kiểm tra được sổ tiết kiệm đang active")
                            break

                        while True:
                            try:
                                actual_months = int(input("Nhập số tháng thực gửi: "))

                                if actual_months <= 0:
                                    print("Số tháng thực gửi phải là số nguyên dương")
                                    continue

                                break

                            except ValueError:
                                print("Số tháng thực gửi phải là số nguyên dương")

                        if actual_months < account["term_months"]:
                            applied_rate = 0.5
                            print("Khách hàng rút trước hạn, áp dụng lãi suất 0.5%/năm")
                        else:
                            applied_rate = account["interest_rate"]
                            print("Khách hàng đủ kỳ hạn, áp dụng lãi suất ban đầu")

                        interest_money = (
                            account["balance"]
                            * applied_rate
                            / 100
                            * actual_months
                            / 12
                        )

                        total_receive = account["balance"] + interest_money

                        print("\n===== KẾT QUẢ KIỂM TRA RÚT TIỀN =====")
                        print(f"Mã sổ: {account['account_id']}")
                        print(f"Khách hàng: {account['customer_name']}")
                        print(f"Số tiền gửi: {account['balance']:,} VND")
                        print(f"Số tháng thực gửi: {actual_months} tháng")
                        print(f"Lãi suất áp dụng: {applied_rate}%/năm")
                        print(f"Tiền lãi thực nhận: {interest_money:,.0f} VND")
                        print(f"Tổng tiền thực nhận: {total_receive:,.0f} VND")

                        break

                if not is_found:
                    print("Không tìm thấy mã sổ tiết kiệm!")
                            

            case 7:
                print("Thoát chương trình.")
                break

    except ValueError:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")