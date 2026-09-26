"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class VesselBerthEntry(BaseModel):
    """靠泊计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 船名
    field_2: str | None = None  # 航次
    field_3: str | None = None  # 预计到港
    field_4: str | None = None  # 实际到港
    field_5: str | None = None  # 泊位编号
    field_6: str | None = None  # 靠泊方向
    field_7: str | None = None  # 计划状态

class QuayCraneEntry(BaseModel):
    """岸桥明细结构。"""

    field_0: str | None = None  # 岸桥编号
    field_1: str | None = None  # 岸桥类型
    field_2: str | None = None  # 额定起重量
    field_3: str | None = None  # 作业泊位
    field_4: str | None = None  # 当前船名
    field_5: str | None = None  # 作业箱量
    field_6: str | None = None  # 司机
    field_7: str | None = None  # 岸桥状态

class ContainerEntry(BaseModel):
    """集装箱明细结构。"""

    field_0: str | None = None  # 箱号
    field_1: str | None = None  # 箱型尺寸
    field_2: str | None = None  # 箱主代码
    field_3: str | None = None  # 铅封号
    field_4: str | None = None  # 毛重
    field_5: str | None = None  # 目的港
    field_6: str | None = None  # 空重标识
    field_7: str | None = None  # 箱状态

class YardSlotEntry(BaseModel):
    """堆场箱位明细结构。"""

    field_0: str | None = None  # 箱位编号
    field_1: str | None = None  # 堆场区号
    field_2: str | None = None  # 排号
    field_3: str | None = None  # 列号
    field_4: str | None = None  # 层高
    field_5: str | None = None  # 箱型限制
    field_6: str | None = None  # 当前箱号
    field_7: str | None = None  # 箱位状态

class YardCraneEntry(BaseModel):
    """场桥明细结构。"""

    field_0: str | None = None  # 场桥编号
    field_1: str | None = None  # 场桥类型
    field_2: str | None = None  # 额定起重量
    field_3: str | None = None  # 作业堆场
    field_4: str | None = None  # 当前任务
    field_5: str | None = None  # 司机
    field_6: str | None = None  # 燃料余量
    field_7: str | None = None  # 场桥状态

class TruckEntry(BaseModel):
    """集卡明细结构。"""

    field_0: str | None = None  # 车辆编号
    field_1: str | None = None  # 车牌号
    field_2: str | None = None  # 当前任务
    field_3: str | None = None  # 当前位置
    field_4: str | None = None  # 计划路线
    field_5: str | None = None  # 司机
    field_6: str | None = None  # 载箱状态
    field_7: str | None = None  # 车辆状态

class GateEntry(BaseModel):
    """闸口记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 箱号
    field_2: str | None = None  # 车牌号
    field_3: str | None = None  # 进出方向
    field_4: str | None = None  # 过闸时间
    field_5: str | None = None  # 货重
    field_6: str | None = None  # 验残结果
    field_7: str | None = None  # 闸口状态

class DangerousEntry(BaseModel):
    """危品申报明细结构。"""

    field_0: str | None = None  # 申报编号
    field_1: str | None = None  # 箱号
    field_2: str | None = None  # 危险品类别
    field_3: str | None = None  # UN编号
    field_4: str | None = None  # 应急措施
    field_5: str | None = None  # 堆存区位
    field_6: str | None = None  # 温度监测
    field_7: str | None = None  # 申报状态

class ReeferEntry(BaseModel):
    """冷藏箱明细结构。"""

    field_0: str | None = None  # 箱号
    field_1: str | None = None  # 设定温度
    field_2: str | None = None  # 实时温度
    field_3: str | None = None  # 供电桩号
    field_4: str | None = None  # 插电时间
    field_5: str | None = None  # 报警阈值
    field_6: str | None = None  # 巡检记录
    field_7: str | None = None  # 箱状态

class PowerStationEntry(BaseModel):
    """供电桩明细结构。"""

    field_0: str | None = None  # 桩号
    field_1: str | None = None  # 桩位地址
    field_2: str | None = None  # 额定功率
    field_3: str | None = None  # 当前负载
    field_4: str | None = None  # 占用箱号
    field_5: str | None = None  # 占用时间
    field_6: str | None = None  # 维护记录
    field_7: str | None = None  # 桩状态

class StevedoreEntry(BaseModel):
    """装卸班组明细结构。"""

    field_0: str | None = None  # 班组编号
    field_1: str | None = None  # 班组名称
    field_2: str | None = None  # 班组长
    field_3: str | None = None  # 在岗人数
    field_4: str | None = None  # 作业船舶
    field_5: str | None = None  # 当前任务
    field_6: str | None = None  # 交接时段
    field_7: str | None = None  # 班组状态

class TariffEntry(BaseModel):
    """结算单明细结构。"""

    field_0: str | None = None  # 结算单号
    field_1: str | None = None  # 船名航次
    field_2: str | None = None  # 箱量合计
    field_3: str | None = None  # 堆存天数
    field_4: str | None = None  # 装卸费
    field_5: str | None = None  # 堆存费
    field_6: str | None = None  # 应收总额
    field_7: str | None = None  # 结算状态

class TideEntry(BaseModel):
    """潮汐记录明细结构。"""

    field_0: str | None = None  # 记录日期
    field_1: str | None = None  # 潮时
    field_2: str | None = None  # 潮高
    field_3: str | None = None  # 风速
    field_4: str | None = None  # 风向
    field_5: str | None = None  # 能见度
    field_6: str | None = None  # 浪高
    field_7: str | None = None  # 记录状态

class AccidentEntry(BaseModel):
    """事故记录明细结构。"""

    field_0: str | None = None  # 事故编号
    field_1: str | None = None  # 事故类型
    field_2: str | None = None  # 发生时间
    field_3: str | None = None  # 涉事设备
    field_4: str | None = None  # 受伤人数
    field_5: str | None = None  # 影响范围
    field_6: str | None = None  # 处置措施
    field_7: str | None = None  # 事故状态

class EquipmentEntry(BaseModel):
    """保养计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 设备编号
    field_2: str | None = None  # 保养内容
    field_3: str | None = None  # 计划日期
    field_4: str | None = None  # 保养周期
    field_5: str | None = None  # 保养班组
    field_6: str | None = None  # 上次保养日
    field_7: str | None = None  # 计划状态

class PilotEntry(BaseModel):
    """引航任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 船名
    field_2: str | None = None  # 引航员
    field_3: str | None = None  # 引航区域
    field_4: str | None = None  # 上船时间
    field_5: str | None = None  # 下船时间
    field_6: str | None = None  # 引航里程
    field_7: str | None = None  # 任务状态

class CustomsEntry(BaseModel):
    """查验记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 箱号
    field_2: str | None = None  # 查验类型
    field_3: str | None = None  # 布控时间
    field_4: str | None = None  # 放行时间
    field_5: str | None = None  # 查验结果
    field_6: str | None = None  # 查验科员
    field_7: str | None = None  # 查验状态

class ShiftLogEntry(BaseModel):
    """工班日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 工班日期
    field_2: str | None = None  # 班次
    field_3: str | None = None  # 值班调度
    field_4: str | None = None  # 船舶动态
    field_5: str | None = None  # 作业概况
    field_6: str | None = None  # 遗留事项
    field_7: str | None = None  # 日志状态
