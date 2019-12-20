from django.db import models
from django.utils.translation import ugettext_lazy as _


class History(models.Model):
    date = models.DateTimeField(_('Date'))
    search = models.CharField(_(u'Search'), max_length=140)
    
    class Meta:
        verbose_name = _('History')
        verbose_name_plural = _('Historys')
        db_table = 'history'
