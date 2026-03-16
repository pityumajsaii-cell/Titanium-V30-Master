from ai_router import launch_full_system, launch_growth_monitor
import os
os.environ["PYTHONPATH"] = os.path.expanduser("~/titanium_v11")

launch_full_system(
    modules=["Education","AI_Tools","AI_Marketing","Payment","Dashboard"],
    mobile_friendly=True,
    push_notifications=True,
    realtime_graphs=True,
    analytics=True,
    self_learning=True,
    auto_archive=True
)

launch_growth_monitor()
