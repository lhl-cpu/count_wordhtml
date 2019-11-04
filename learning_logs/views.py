from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, 'index.html')


def count(request):
	count_total = len(request.GET['text'])
	comtext = request.GET['text']

	word_dict = {}
	for word in comtext:
		if word not in word_dict:
			word_dict[word] = 1
		else:
			word_dict[word] += 1
	sorted_dict = sorted(word_dict.items(), key = lambda w:w[1],reverse=True)

	return render(request, 'count.html',
		{
		'count':count_total,
		'text':comtext,
		'worddict':word_dict,
		'sortdict':sorted_dict
		})
