from django.contrib import admin
from accounts.models import User, OTP
from datasets.models import Dataset
from competitions.models import Competition, Submission
from leaderboard.models import LeaderboardEntry
from discussion.models import DiscussionThread, DiscussionPost
from mpesa.models import MpesaTransaction

admin.site.register(User)
admin.site.register(OTP)
admin.site.register(Dataset)
admin.site.register(Competition)
admin.site.register(Submission)
admin.site.register(LeaderboardEntry)
admin.site.register(DiscussionThread)
admin.site.register(DiscussionPost)
admin.site.register(MpesaTransaction)
