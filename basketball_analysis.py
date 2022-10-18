import pandas as pd
import math


def y_3_point(x_value):
    return math.sqrt(23.75**2 - x_value**2)


def percentage_2pt_attempt(data):
    total = len(data)
    total_2pt = 0
    df = data[(data["x"] <= 22) & (data["x"] >= -22)]
    for x_val, y_val in zip(df["x"], df["y"]):
        if y_val <= 7.8:
            total_2pt += 1
        elif y_val > 7.8:
            if y_val < y_3_point(x_val):
                total_2pt += 1
    print(total_2pt / total)


def percentage_nc3_attempt(data):
    total = len(data)
    total_nc3_curve = 0
    df_line = data[(data["x"] > 22) | (data["x"] < -22)]
    df_line = df_line[(df_line["y"] > 0) & (df_line["y"] <= 7.8)]
    df_curve = data[(data["y"] > 7.8)]
    total_nc3_line = len(df_line)
    for x_val, y_val in zip(df_curve["x"], df_curve["y"]):
        if y_val > y_3_point(x_val):
            total_nc3_curve += 1
    total_nc3_attempt = total_nc3_line + total_nc3_curve
    print(total_nc3_attempt / total)


def percentage_c3_attempt(data):
    total = len(data)
    df = data[(data["x"] > 22) | (data["x"] < -22)]
    df = df[df["y"] <= 0]
    print(len(df) / total)


def eFG_2pt(data):
    df = data[(data["x"] <= 22) & (data["x"] >= -22)]
    total = 0
    num_attempt = 0
    for x_val, y_val, fg in zip(df["x"], df["y"], df["fgmade"]):
        if y_val <= 7.8:
            total += 1
            if fg == 1:
                num_attempt += 1
        elif y_val > 7.8:
            if y_val < y_3_point(x_val):
                total += 1
                if fg == 1:
                    num_attempt += 1
    print(num_attempt / total)


def eFG_nc3(data):
    df_line = data[(data["x"] > 22) | (data["x"] < -22)]
    df_line = df_line[(df_line["y"] > 0) & (df_line["y"] <= 7.8)]
    df_curve = data[(data["y"] > 7.8)]
    total_nc3_line = len(df_line)
    num_curve_nc3 = 0
    total_curve_nc3 = 0
    for x_val, y_val, fg in zip(df_curve["x"], df_curve["y"], df_curve["fgmade"]):
        if y_val > y_3_point(x_val):
            total_curve_nc3 += 1
            if fg == 1:
                num_curve_nc3 += 1
    df_line = df_line[df_line["fgmade"] == 1]
    num_line_nc3 = len(df_line)

    total_nc3_made = num_line_nc3 + num_curve_nc3
    total_attempt = total_nc3_line + total_curve_nc3

    print(total_nc3_made / total_attempt)


def eFG_c3(data):
    df = data[(data["x"] > 22) | (data["x"] < -22)]
    df = df[df["y"] <= 0]
    num_c3_attempt = len(df)
    df_c3_made = df[df["fgmade"] == 1]
    num_c3_made = len(df_c3_made)
    print(num_c3_made / num_c3_attempt)


def main():
    df = pd.read_csv("shots_data.csv")
    df_A = df[df["team"] == "Team A"]
    df_B = df[df["team"] == "Team B"]

    percentage_2pt_attempt(df_A)
    percentage_2pt_attempt(df_B)
    percentage_nc3_attempt(df_A)
    percentage_nc3_attempt(df_B)
    percentage_c3_attempt(df_A)
    percentage_c3_attempt(df_B)
    eFG_2pt(df_A)
    eFG_2pt(df_B)
    eFG_nc3(df_A)
    eFG_nc3(df_B)
    eFG_c3(df_A)
    eFG_c3(df_B)


if __name__ == "__main__":
    main()