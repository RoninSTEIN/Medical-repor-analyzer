
def comparison(report_num, upper_limit, lower_limit, name):
    if report_num < lower_limit:
        print(
            f"The Blood is defficient in {name} The diagnosed number should be MORE than {lower_limit} but is {report_num} please seek medical attention ")

    if report_num > upper_limit:
        print(
            f"The Blood has exessive {name} The Diagnosed number should be Less than {upper_limit} but is {report_num} please seek medical attention")

    if report_num == lower_limit or report_num == upper_limit:
        print(
            f"The Blood barely fulffills the optimal conditions for {name}.Please seek medical attention ")

    if report_num > lower_limit and report_num < upper_limit:
        print(f"The Test results are of Optimal condition for {name}")


print("To Check cholestrol condition from your medical report please Enter th values For asked Report elments ")
try:
    total_cholestrol = float(input("TOTAL Cholestrol : "))

except:
    print("ERROR Wrong value")

comparison(total_cholestrol, 200, 0, "Total Cholestrol")

try:
    triglycerides = float(input("TRIGLYCERIDES : "))

except:
    print("ERROR Wrong value")

comparison(triglycerides, 150, 0, "TRIGLYCERIDES")

try:
    hdl_cholestrol = float(input("hdl_cholestrols : "))

except:
    print("ERROR Wrong value")

comparison(hdl_cholestrol, 60, 40, "HDL Cholestrol")

try:
    ldl_cholestrol = float(input("LDL Cholestrol : "))

except:
    print("ERROR Wrong value")

comparison(ldl_cholestrol, 100, 0, "LDL Cholestrol")

try:
    vldl_cholestrol = float(input("VLDL Cholestrol : "))

except:
    print("ERROR Wrong value")

comparison(vldl_cholestrol, 40, 5, "VLDL Cholestrol")

try:
    ldl_hdl_ratio = float(input("LDL/HDL RATIO : "))

except:
    print("ERROR Wrong value")

comparison(ldl_hdl_ratio, 5.5, 0.3, "LDL/HDL RATIO")
