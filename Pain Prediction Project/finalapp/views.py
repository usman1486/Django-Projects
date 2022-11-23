from django.shortcuts import render
from .models import PainPrediction
from joblib import load
import random
model = load('./ML_Model/model.joblib')


def index(request):

    return render(request, 'index.html')


def processdata(request):

    seat_h = request.POST.get('seat_height')
    seat_d = request.POST.get('seat_depth')
    seat_w = request.POST.get('seat_width')
    backrest_h = request.POST.get('backrest_h')
    backrest_w = request.POST.get('backrest_w')
    backrest_l = request.POST.get('backrest_l')
    arm_h = request.POST.get('arm_h')
    arm_l = request.POST.get('arm_l')
    arm_distance = request.POST.get('arm_distance')
    age = request.POST.get('age')

    form = PainPrediction(seat_h=seat_h, seat_d=seat_d, seat_w=seat_w, backrest_h=backrest_h, backrest_w=backrest_w,
                          backrest_l=backrest_l, arm_h=arm_h, arm_l=arm_l, arm_distance=arm_distance, age=age)
    form.save()

    result = model.predict(
        [[seat_h, seat_d, seat_w, backrest_h, backrest_w, backrest_l, arm_h, arm_l, arm_distance, age]])

    input_data = {
        'seat_h': seat_h,
        'seat_d': seat_d,
        'seat_w': seat_w,
        'backrest_h': backrest_h,
        'backrest_w': backrest_w,
        'backrest_l': backrest_l,
        'arm_h': arm_h,
        'arm_l': arm_l,
        'arm_distance': arm_distance,
        'age': age
    }
    if result[0, 0] == 1:

        Pain_in_Next_12_months = "Yes"
    else:

        Pain_in_Next_12_months = "No"

    if result[0, 1] == 1:
        Pain_in_Next_4_weeks = "Yes"
    else:

        Pain_in_Next_4_weeks = "No"

    if result[0, 2] == 1:
        Pain_in_Next_few_days = "Yes"
    else:
        Pain_in_Next_few_days = "No"

    if result[0, 3] == 1:
        prevent_work_in_next_12_months = "Yes"
    else:
        prevent_work_in_next_12_months = "No"

    if result[0, 4] == 1:
        seen_doctor_in_next_12_months = "Yes"
    else:
        seen_doctor_in_next_12_months = "No"

    if result[0, 5] == 1:
        taken_medicine = "Yes"
    else:
        taken_medicine = "No"

    if result[0, 6] == 1:
        taken_sick_leave = "Yes"
    else:
        taken_sick_leave = "No"

    if result[0, 7] == 1:
        neck_pain = "Yes"
    else:
        neck_pain = "No"

    if result[0, 8] == 1:
        shoulder_pain = "Yes"
    else:
        shoulder_pain = "No"

    if result[0, 9] == 1:
        low_back_pain = "Yes"
    else:
        low_back_pain = "No"

    if result[0, 10] == 1:
        upper_back_pain = "Yes"
    else:
        upper_back_pain = "No"

    if result[0, 11] == 1:
        elbow = "Yes"
    else:
        elbow = "No"

    if result[0, 12] == 1:
        hands = "Yes"
    else:
        hands = "No"

    if result[0, 13] == 1:
        hips = "Yes"
    else:
        hips = "No"

    if result[0, 14] == 1:
        knees = "Yes"
    else:
        knees = "No"

    if result[0, 15] == 1:
        ankles = "Yes"
    else:
        ankles = "No"

    final_res = {
        'Pain_in_Next_12_months': Pain_in_Next_12_months,
        'Pain_in_Next_4_weeks': Pain_in_Next_4_weeks,
        'Pain_in_Next_few_days': Pain_in_Next_few_days,
        'prevent_work_in_next_12_months': prevent_work_in_next_12_months,
        'seen_doctor_in_next_12_months': seen_doctor_in_next_12_months,
        'taken_medicine': taken_medicine,
        'taken_sick_leave': taken_sick_leave,
        'neck_pain': neck_pain,
        'shoulder_pain': shoulder_pain,
        'low_back_pain': low_back_pain,
        'upper_back_pain': upper_back_pain,
        'elbow': elbow,
        'hands': hands,
        'hips': hips,
        'knees': knees,
        'ankles': ankles

    }

    return render(request, "userform.html", {'data': final_res, 'inp_data': input_data})
