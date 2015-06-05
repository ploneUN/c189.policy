from collective.grok import gs
from c189.policy import MessageFactory as _
from collective.setuphelpers.structure import setupStructure,clearUpSite

@gs.importstep(
    name=u'c189.policy', 
    title=_('c189.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('c189.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
    # STRUCTURE = [{'title':'Stickers',
    #     		'type':'ilo.socialsticker.stickers'}] 
    # setupStructure(portal, STRUCTURE)
  
