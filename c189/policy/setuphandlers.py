from collective.grok import gs
from c189.policy import MessageFactory as _

@gs.importstep(
    name=u'c189.policy', 
    title=_('c189.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('c189.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
