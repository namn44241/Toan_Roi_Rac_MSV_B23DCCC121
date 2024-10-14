# Cho số tự nhiên n (1 <= n <= 10^6).
# Hãy tính số cách lắc xúc xắc 6 mặt có tổng các mặt của mỗi lần xắc bằng 2𝑛.
# Kết quả lấy dư của phép chia cho 10^9+7

def tinh(n):
    MOD = 10 ** 9 + 7
    D = [0] * (2 * n + 1)
    D[0] = 1

    for i in range(1, 2 * n + 1):
        D[i] = 0
        for j in range(1, 7):
            if i - j >= 0:
                D[i] = (D[i] + D[i - j]) % MOD

    return D[2 * n]


def main():
    n = int(input("Nhập n: "))

    if 1 <= n <= 10 ** 6:
        a = tinh(n)
        print(f"Số cách lắc xúc xắc để có tổng bằng 2n là: {a}")
    else:
        print("Giá trị của n không hợp lệ.")


if __name__ == "__main__":
    main()
