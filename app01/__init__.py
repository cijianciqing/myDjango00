

#这个应用的model包含图片，前端templates同样需要类似的考量

#需要注意，如果model的image.url为空，可能导致前端报错
    #raise ValueError("The '%s' attribute has no file associated with it." % self.field.name)

#解决方案
# <img src="{{ article.img.url|default_if_none:'#' }}" alt="图片打开失败" />

# @property
# # def img_url(self):
# #     if self.img and hasattr(self.img, 'url'):
