import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from django.conf import settings
from .forms import UploadFileForm

def handle_uploaded_file(file):
    file_path = os.path.join(settings.MEDIA_ROOT, file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            data = pd.read_csv(file_path)

            # Perform data analysis here
            summary_stats = data.describe().to_html()
            first_rows = data.head().to_html()
            missing_values = data.isnull().sum().to_frame(name='Missing Values').to_html()

            # Generate visualizations
            #
            # sns.set(style="darkgrid")
            # fig, ax = plt.subplots()
            # data.hist(ax=ax)
            # fig.savefig(os.path.join(settings.MEDIA_ROOT, 'histogram.png'))
            #
            sns.set(style="darkgrid")
            fig, ax = plt.subplots(figsize=(10, 8))  # Adjust figure size
            data.hist(ax=ax, bins=20, edgecolor='black', alpha=0.7)  # Adjust bins, edgecolor, and transparency
            plt.tight_layout()  # Adjust layout to ensure no clipping
            fig.savefig(os.path.join(settings.MEDIA_ROOT, 'histogram.png'))

            return render(request, 'analysis/results.html', {
                'summary_stats': summary_stats,
                'first_rows': first_rows,
                'missing_values': missing_values,
                'histogram': 'media/histogram.png',
            })
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
