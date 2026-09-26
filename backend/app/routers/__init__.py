"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import vessel_berth as router_vessel_berth
from app.routers import quay_crane as router_quay_crane
from app.routers import container as router_container
from app.routers import yard_slot as router_yard_slot
from app.routers import yard_crane as router_yard_crane
from app.routers import truck as router_truck
from app.routers import gate as router_gate
from app.routers import dangerous as router_dangerous
from app.routers import reefer as router_reefer
from app.routers import power_station as router_power_station
from app.routers import stevedore as router_stevedore
from app.routers import tariff as router_tariff
from app.routers import tide as router_tide
from app.routers import accident as router_accident
from app.routers import equipment as router_equipment
from app.routers import pilot as router_pilot
from app.routers import customs as router_customs
from app.routers import shift_log as router_shift_log

ROUTERS = [router_vessel_berth, router_quay_crane, router_container, router_yard_slot, router_yard_crane, router_truck, router_gate, router_dangerous, router_reefer, router_power_station, router_stevedore, router_tariff, router_tide, router_accident, router_equipment, router_pilot, router_customs, router_shift_log]
