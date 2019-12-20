from django.db import models
from django.utils.translation import ugettext_lazy as _


class History(models.Model):
    date = models.DateTimeField(_('Date'), auto_now_add=True)
    search = models.CharField(_(u'Search'), max_length=140)
    json = models.TextField(_('Json'))
    
    class Meta:
        verbose_name = _('History')
        verbose_name_plural = _('Historys')
        db_table = 'history'
        ordering = ['-date']
