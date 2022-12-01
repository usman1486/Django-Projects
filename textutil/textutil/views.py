from django.shortcuts import redirect, render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    text = request.GET.get('content')
    removepunc = request.GET.get('Removepunctuation')
    caps = request.GET.get('caps')
    space = request.GET.get('space')
    lowercase = request.GET.get('lowercase')
    count = request.GET.get('count')
    newline = request.GET.get('newline')
    purpose = ""

    punc = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
    if removepunc == 'on':
        purpose += '|removepunc|'
        analyzed = ""
        for char in text:
            if char not in punc:
                analyzed = analyzed+char
                data = {'analyzed': analyzed,
                        'purpose': purpose


                        }
                text = analyzed

    if caps == 'on':
        analyzed = " "
        purpose += "|caps|"
        for char in text:
            analyzed = analyzed+char.upper()
            data = {'analyzed': analyzed,
                    'purpose': purpose
                    }
            text = analyzed

    if space == 'on':
        analyzed = " "
        purpose += '|ExtraspaceRemover|'
        for index, char in enumerate(text):
            if text[index] == "" and text[index+1] == "":
                pass
            else:
                analyzed = analyzed+char
                data = {'analyzed': analyzed,
                        'purpose': purpose
                        }
                text = analyzed

    if lowercase == 'on':
        analyzed = " "
        purpose += '|lowercase|'
        for char in text:
            analyzed = analyzed+char.lower()
            data = {'analyzed': analyzed,
                    'purpose': purpose
                    }
            text = analyzed

    if newline == 'on':
        analyzed = " "
        purpose += '|NewLineRemove|'
        for char in text:
            if char != '\n' and char != '\r':
                analyzed = analyzed+char
                data = {'analyzed': analyzed,
                        'purpose': purpose
                        }
                text = analyzed

    if count == 'on':
        analyzed = " "
        purpose += '|count|'
        res = sum(not chr.isspace() for chr in text)
        analyzed = str(res)
        data = {'analyzed': analyzed,
                'purpose': purpose
                }
    if count != 'on' and newline != 'on' and lowercase != 'on' and caps != 'on' and space != 'on' and removepunc != 'on':
        return redirect('index')
    return render(request, 'view.html', {"data": data})
