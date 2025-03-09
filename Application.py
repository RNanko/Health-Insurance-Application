import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from tkinter import *
import pandas as pd
from joblib import load

def weight_show(e):
    weight_scaler_label.config(text=f"{round(weight_scaler.get())} Kg", font=font3)

def height_show(e):
    height_scaler_label.config(text=f"{round(height_scaler.get(), 2)} Sm", font=font3)

def bmi_calculator(w, h):
    # BMI calculator
    return round(w/(h*h),1)

def bmi_calc_btn():
    # GET calculated BMI value from data
    try:
        bmi_val = bmi_calculator(weight_scaler.get(), height_scaler.get())
        bmi.delete(0, END)
        bmi.insert(0,f"{bmi_val}")
        bmi_label.config(text=f"BMI: {bmi_range(bmi_val)}")
        bmi.config(font=("Arial", "10", "bold"), foreground="white")
        bmi_label.config(foreground="white")
    except:
        bmi.config(font=("Arial", "10", "bold"), foreground="red")
        bmi.insert(0, "No Data Error!")

def bmi_range(bmi):
    # Labels ranged by BMI values
    if bmi < 16:
        return "Severe Thinness"
    elif 16 <= bmi < 17:
        return "Moderate Thinness"
    elif 17 <= bmi < 18.5:
        return "Mild Thinness"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese Class I"
    elif 35 <= bmi < 40:
        return "Obese Class II"
    else:  # bmi >= 40
        return "Obese Class III"

def calculate():
    # Visual label convertor
    regions = {"Southwest": "region_southwest",
               "Southeast": "region_southeast",
               "Northwest": "region_northwest",
               "Northeast": "region_northeast"}
    # Data for ML model
    sample = {
        'age': None,
        'bmi': None,
        'children': None,
        'smoker': None,
        'region_northeast': 0,
        'region_northwest': 0,
        'region_southeast': 0,
        'region_southwest': 0,
        'sex_female': None,
        'sex_male': None
    }

    # Get data from Enter fields
    try:

        # Get Age
        if not age.get().isdigit():
            age_label.configure(text="PROVIDE THE AGE:", foreground="red")
        else:
            age_label.configure(text="AGE SELECTED", foreground="green")
            sample['age'] = int(age.get())

        # Get Gender
        if sex_var.get() == "M":
            sample["sex_female"] = 0
            sample["sex_male"] = 1
            sex_label.configure(text="GENDER SELECTED", foreground="green")
        elif sex_var.get() == "W":
            sample["sex_female"] = 1
            sample["sex_male"] = 0
            sex_label.configure(text="GENDER SELECTED", foreground="green")
        else:
            sex_label.configure(text="PLEASE SELECT GENDER:", foreground="red")

        # Get children number
        if not children.get().isdigit():
            children_label.configure(text="PROVIDE CHILDREN QUANTITY:", foreground="red")
        else:
            children_label.configure(text="NUMBER SELECTED", foreground="green")
            sample['children'] = int(children.get())

        # Get 1 if smoker
        sample["smoker"] = 1 if smoker_var.get() else 0

        # Get BMI
        if not bmi.get() or bmi.get() == "No Data Error!":
            bmi_label.config(text="BMI (ENTER OR CALCULATE):", foreground="red")
        else:
            bmi_label.config(text="BMI SELECTED", foreground="green")
            bmi.config(font=("Arial", "10", "bold"), foreground="white")
            sample['bmi'] = float(bmi.get())

        # Get Region
        if selected_region.get() not in regions:
            region_label.config(text="SELECT REGION:", foreground="red")
        else:
            sample[regions[selected_region.get()]] = 1
            region_label.config(text="REGION SELECTED", foreground="green")

        # Load the ML model safely
        try:
            # Option to save/load model using pickle or joblib
            # with open("insurance_model.pkl", "rb") as f:
            #     stacking_regressor = pickle.load(f)
            stacking_regressor = load("insurance_model.joblib")
        except FileNotFoundError:
            exception_label.configure(text="Error: Model file not found!")
            return

        # Dict to frame
        sample_df = pd.DataFrame([sample])

        # Make Prediction
        prediction = stacking_regressor.predict(sample_df)

        # Update UI with prediction
        charges.configure(text=f"{prediction[0]:.2f} $")  # Format to 2 decimal places

        # Empty exception filed - NO ERROR
        exception_label.configure(text=f"")

    except Exception as e:
        exception_label.configure(text=f"Error!")




root = tb.Window(themename="superhero")
root.title("DB")
root.geometry("600x900")

font1 = ("Arial", "16", "bold")
font2 = ("Arial", "12")
font3 = ("Arial", "10", 'italic')

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

main_label = tb.Label(root, text="Health Insurance Calculator", font=font1)
main_label.grid(row=0, column=0, padx=10, pady=20, columnspan=3, sticky="N")  # Centered

# Age
age_label = tb.Label(root, text="Age:", font=font2)
age_label.grid(row=1, column=0, padx=10, pady=20, sticky="N")
age = tb.Entry(root, width=25, font=font3, justify='center')
age.grid(row=1, column=1, padx=20, pady=20, columnspan=2)

# Man/Woman
sex_var = StringVar(value="")
sex_label = tb.Label(root, text="Select Gender:", font=font2)
sex_label.grid(row=2, column=0, padx=10, pady=10, sticky="N")

# Man/Woman
style = tb.Style()
style.configure("Custom.TRadiobutton", font=font2)

sexm = tb.Radiobutton(root, variable=sex_var, value="M", text="Man",
                      style="Custom.TRadiobutton")
sexm.grid(row=2, column=1, padx=10, pady=10, sticky="N")
sexf = tb.Radiobutton(root, variable=sex_var, value="W", text="Woman",
                      style="Custom.TRadiobutton")
sexf.grid(row=2, column=2, padx=10, pady=10, sticky="N")

# BMI
bmi_label = tb.Label(root, text="BMI (Enter or calculate):", font=font2, width=27, anchor=CENTER)
bmi_label.grid(row=3, column=0, padx=10, pady=15, sticky="N")
bmi = tb.Entry(root, width=25, font=font3, justify='center')
bmi.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

# BMI - weight
weight_label = tb.Label(root, text="Weight:", font=font3)
weight_label.grid(row=4, column=0, rowspan=2, padx=10, pady=10)
weight_scaler_label = tb.Label(root, text="kg", font=font3)
weight_scaler_label.grid(row=4, column=1, columnspan=2, padx=10, pady=10, sticky="N")
weight_scaler = tb.Scale(root, bootstyle=INFO, length=200, from_=40, to=140, command=weight_show)
weight_scaler.grid(row=5, column=1, columnspan=2, padx=10, pady=10, sticky="N")

# BMI - height
height_label = tb.Label(root, text="Height:", font=font3)
height_label.grid(row=6, column=0, rowspan=2, padx=10, pady=10)
height_scaler_label = tb.Label(root, text="m", font=font3)
height_scaler_label.grid(row=6, column=1, columnspan=2, padx=10, pady=10, sticky="N")
height_scaler = tb.Scale(root, bootstyle=INFO, length=200, from_=1.40, to=2.10, command=height_show)
height_scaler.grid(row=7, column=1, columnspan=2, padx=10, pady=10, sticky="N")

# BMI - Calculate
style.configure('success.Outline.TButton', font=font2)
bmi_btn_calc = tb.Button(root, text="Calculate BMI", width=50, style='success.Outline.TButton',
                         command=bmi_calc_btn)
bmi_btn_calc.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

# Children
children_label = tb.Label(root, text="Children quantity:", font=font2)
children_label.grid(row=9, column=0, padx=10, pady=20)
children = tb.Entry(root, width=25, font=font3, justify='center')
children.grid(row=9, column=1, padx=10, pady=20, columnspan=2)

# Smoker
smoker_label = tb.Label(root, text="Smoker?", font=font2)
smoker_label.grid(row=10, column=0, padx=10, pady=20)
style.configure('success.TCheckbutton', font=font2)
smoker_var = IntVar()
smoker = tb.Checkbutton(root, text="Yes", onvalue=1, offvalue=0, style='success.TCheckbutton',
                        variable=smoker_var)
smoker.grid(row=10, column=1, padx=10, pady=20, columnspan=2)

# Region
regions = ["Southwest", "Southeast", "Northwest", "Northeast"]
selected_region = StringVar()
selected_region.set("Select region")
region_label = tb.Label(root, text="Region:", font=font2)
region_label.grid(row=11, column=0, padx=10, pady=20)
region = tb.Combobox(root, bootstyle=SUCCESS, textvariable=selected_region, values=regions,
                     justify="center", state="readonly", font=font2)
region.grid(row=11, column=1, padx=10, pady=20, columnspan=2)

# Frame for charges
frame = Frame(root, height=50, borderwidth=2, relief=SOLID,
              highlightbackground="green", highlightthickness=2)
frame.grid(row=12, column=0, columnspan=3, sticky="ew", padx=20, pady=10)
frame.config(bg="green")

frame.grid_columnconfigure(1, weight=1)

style.configure("Custom.TButton", font=font1, background="#000000", bordercolor="#000000",
                relief=SOLID)
style.map("Custom.TButton", background=[("active", "green")])
charges_btn = tb.Button(frame, text="Calculate Costs", style="Custom.TButton", command=calculate)
charges_btn.grid(column=0, row=0, padx=10, pady=20, ipadx=50)
charges = tb.Label(frame, text="0.00 $", font=font1, foreground="red", background="green",
                   anchor=CENTER)
charges.grid(column=1, row=0, padx=10, pady=20)


ToolTip(charges_btn, text="Run Prediction", bootstyle=(SECONDARY, INVERSE))



exception_label = tb.Label(root, text="", font=font2, foreground="red",
                           width=50, wraplength=500)
exception_label.grid(column=0, row=13, padx=10, pady=20, columnspan=3)


root.mainloop()

