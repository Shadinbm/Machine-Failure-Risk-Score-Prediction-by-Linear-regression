from sklearn.linear_model import LinearRegression
import pandas as pd
df=pd.read_csv('dat.csv')
x=df[['temperature_celsius','vibration_mm_per_sec','pressure_bar','motor_current_amp','oil_temperature_celsius','rotational_speed_rpm','power_consumption_kw']]
y=df['failure_risk_score']
ob=LinearRegression()
ob.fit(x,y)
# print(ob.score(x,y))
temp=float(input("enter temprature:"))
vib=float(input("enter vibraton:"))
pres=float(input("enter pressure:"))
mot=float(input("enter motor_current:"))
oil=float(input("enter oil temprature:"))
rot=float(input("enter rotaion speed rpm:"))
pow=float(input("enter power consumption:"))
pred=ob.predict([[temp,vib,pres,mot,oil,rot,pow]])
print("Machine failure Risk Score=",pred)
if pred<50:
    print("Good Conditon")
elif 50<pred<90:
    print("maintance reqiured")
elif pred >90:
    print("Critical Condition,high risk of failure")
new = pd.DataFrame([{
    'temperature_celsius': temp,
    'vibration_mm_per_sec': vib,
    'pressure_bar': pres,
    'motor_current_amp': mot,
    'oil_temperature_celsius': oil,
    'rotational_speed_rpm': rot,
    'power_consumption_kw': pow,
    'failure_risk_score': pred[0]
}])
ex=pd.read_csv('new.csv')
