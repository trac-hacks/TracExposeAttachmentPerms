from trac.core import *
from trac.perm import IPermissionRequestor

class ExposeAttachmentPermsModule(Component):
    """A permission requestor to expose the Attachment component's internal permissions to the admin panel."""

    implements(IPermissionRequestor)

    def get_permission_actions(self):
        return ['ATTACHMENT_VIEW', 'ATTACHMENT_CREATE', 'ATTACHMENT_REMOVE']
