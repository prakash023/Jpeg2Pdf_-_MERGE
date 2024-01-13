#!/usr/bin/env python
# coding: utf-8

# In[56]:


import os
import PyPDF2


# In[57]:


from PIL import Image
from PyPDF2 import PdfFileMerger


# In[58]:


output_dir = 'D:\Python\image2pdf\pdf'


# In[59]:


sources_dir = 'D:\Python\image2pdf\Images'
#, 'D:\Python\image2pdf\pdf\Auf_2.pdf'


# In[60]:


for file in os.listdir(sources_dir):
    if file.split('.')[-1] in('png','jpg', 'jpeg'):
        image = Image.open(os.path.join(sources_dir, file))
        image_converted = image.convert('RGB')
        image_converted.save(os.path.join(output_dir, '{0}.pdf'.format(file.split('.')[-2])))


# In[ ]:


#Now from here merging the pdf files 


# In[61]:


merger = PdfFileMerger()


# In[70]:


pdf_files = ['D:\Python\image2pdf\Auf_1.pdf',
            'D:\Python\image2pdf\pdf\Auf_2.pdf']


# In[72]:


for pdf_file in pdf_files:
    merger.append(pdf_file)


# In[74]:


merger.write("merged_2_pages.pages.pdf")
merger.close()


# In[ ]:




