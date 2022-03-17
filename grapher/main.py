import matplotlib.pyplot as plt


class Grapher:
    def __init__(self, apr: float):
        self.apr = apr

    def compound(self, years: int, start_amount: float = 0, monthly_deposit: float = 0, deposit_increase: float = 0):
        # Set Arrays
        x, y, y2, y3 = [], [], [], []

        deposited, tot = start_amount, start_amount
        earnings = 0
        for i in range(0, years):
            monthly_deposit = monthly_deposit * deposit_increase
            tot = tot * self.apr
            earnings += (deposited * self.apr) - deposited
            for j in range(0, 12):
                tot += monthly_deposit
                deposited += monthly_deposit

                # Add dates
                x.append(i * 12 + j)
                # x2.append(i * 12 + j)
                # x3.append(i * 12 + j)

                # Add amounts
                y.append(tot)
                y2.append(deposited)
                y3.append(earnings + deposited)
        self.generate_graph(x, y, y2, y3, "Compound Interest")
        print(round(tot, 2))
        print(deposited)

    def generate_graph(self, x, y, y2, y3, title):
        plt.plot(x, y, label="Total with compound interest", linestyle='-', linewidth=2, color='#10ab53')
        plt.plot(x, y3, label="Total with simple interest", linestyle="--", linewidth=2, color='#116a37')
        plt.plot(x, y2, label="Total Deposited", linestyle=":", linewidth=2, color='#0e592e')
        plt.xlabel("Time (Months)")
        plt.ylabel("Amount ($)")
        plt.title(title)
        plt.legend()
        plt.show()


interest = Grapher(apr=1.06)
interest.compound(years=30, monthly_deposit=25, start_amount=200, deposit_increase=1.04)
