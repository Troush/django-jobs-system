from django.http import HttpResponse
from django.shortcuts import render
import simplejson
from django.views.decorators.csrf import csrf_exempt
from models import Candidate, Company, Vacancy, JobsCategory

import podunk


def index(request):
    return render(request, 'index.html', locals())

def search(request):
    return render(request, 'search.html', locals())

@csrf_exempt
def ajax_type(request):
    if request:
        data = {}
        selected_type = request.POST.get('type_box')
        if selected_type == 'candidate':
            data = model_to_json(Candidate)
        if selected_type == 'company':
            data = model_to_json(Company)
        return HttpResponse(simplejson.dumps(data), mimetype='application/json')
    return HttpResponse(simplejson.dumps({}), mimetype='application/json')

@csrf_exempt
def ajax_vacancy(request):
    if request.POST:
        data = model_to_json(Vacancy,search_param='company',search_data=request.POST.get('company_id'))
        return HttpResponse(simplejson.dumps(data), mimetype='application/json')
    return HttpResponse(simplejson.dumps({}), mimetype='application/json')
@csrf_exempt
def ajax_search(request):
    if request:
        print request.POST
        if request.POST.get('vacancy_id'):
            print "SDASD"
            vacancy_id = request.POST.get('vacancy_id')
            vacancy = Vacancy.objects.get(pk=vacancy_id)
            search_result = Candidate.objects.filter(looking_for=vacancy.jobs_category,
                                                    location=vacancy.location,
                                                    sex=vacancy.sex,
                                                    education=vacancy.education,
                                                    experience=vacancy.experience,
                                                    )
            if search_result:
                data = []
                json = {}
                print search_result, "SSSADSD"
                for res in search_result:
                    json = {
                    'title': res.name,
                    'email': res.email,
                    'job_category': JobsCategory.objects.get(pk=res.looking_for_id).name,
                    'location': res.location,
                    'experience': res.experience,
                    'keywords': res.more_info
                    }
                    print json
                    data.append(json)
                return HttpResponse(simplejson.dumps(data,indent=4), mimetype='application/json')
        if request.POST.get('candidate_id'):
            candidate_id = request.POST.get('candidate_id')
            candidate = Candidate.objects.get(pk=candidate_id)
            candidate_reg = (candidate.more_info).replace(' ','/').replace(',','/')
            search_result = Vacancy.objects.filter(jobs_category=candidate.looking_for,
                                                    location=candidate.location,
                                                    sex=candidate.sex,
                                                    education=candidate.education,
                                                    experience=candidate.experience,
                                                    )
            if search_result:
                data = []
                json = {}
                print search_result
                for res in search_result:
                    json = {
                    'title': res.title,
                    'company': res.company.name,
                    'job_category': JobsCategory.objects.get(pk=res.jobs_category_id).name,
                    'location': res.location,
                    'experience': res.experience,
                    'keywords': res.keyword
                    }
                    data.append(json)
                return HttpResponse(simplejson.dumps(data,indent=4), mimetype='application/json')
    return HttpResponse(simplejson.dumps({}), mimetype='application/json')

def model_to_json(model,search_param=False,search_data=False):
    data = {}
    i = 1
    if search_param and search_data:
        objs = model.objects.filter([search_param,search_data])
        print objs
    else:
        objs = model.objects.all()
    for obj in objs:
        item = {
            'name': obj.get_name(),
            'cand_id': obj.id,
        }
        data[i] = item
        i += 1
    return data
