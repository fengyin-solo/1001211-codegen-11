# 港口集装箱作业调度管理平台

覆盖船舶靠离、岸桥装卸、堆场箱位、闸口进出、危险品监管、冷藏箱供电及费率结算的港口集装箱全流程作业后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 船舶靠泊 | `vessel_berth` | 靠泊计划 | 计划编号、船名、航次 |
| 岸桥作业 | `quay_crane` | 岸桥 | 岸桥编号、岸桥类型、额定起重量 |
| 集装箱信息 | `container` | 集装箱 | 箱号、箱型尺寸、箱主代码 |
| 堆场箱位 | `yard_slot` | 堆场箱位 | 箱位编号、堆场区号、排号 |
| 场桥调度 | `yard_crane` | 场桥 | 场桥编号、场桥类型、额定起重量 |
| 内集卡调度 | `truck` | 集卡 | 车辆编号、车牌号、当前任务 |
| 闸口管理 | `gate` | 闸口记录 | 记录编号、箱号、车牌号 |
| 危险品监管 | `dangerous` | 危品申报 | 申报编号、箱号、危险品类别 |
| 冷藏箱监控 | `reefer` | 冷藏箱 | 箱号、设定温度、实时温度 |
| 供电桩管理 | `power_station` | 供电桩 | 桩号、桩位地址、额定功率 |
| 装卸队管理 | `stevedore` | 装卸班组 | 班组编号、班组名称、班组长 |
| 费率结算 | `tariff` | 结算单 | 结算单号、船名航次、箱量合计 |
| 潮汐气象 | `tide` | 潮汐记录 | 记录日期、潮时、潮高 |
| 事故处置 | `accident` | 事故记录 | 事故编号、事故类型、发生时间 |
| 设备保养 | `equipment` | 保养计划 | 计划编号、设备编号、保养内容 |
| 引航调度 | `pilot` | 引航任务 | 任务编号、船名、引航员 |
| 海关查验 | `customs` | 查验记录 | 记录编号、箱号、查验类型 |
| 工班日志 | `shift_log` | 工班日志 | 日志编号、工班日期、班次 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
