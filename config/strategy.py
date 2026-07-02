"""
Central Strategy Configuration
Modify only this file to tune the strategy.
"""


# =====================================================
# ACCOUNT SETTINGS
# =====================================================

ACCOUNT_CAPITAL = 100000          # Rs
DEPLOYED_CAPITAL = 40000          # Rs

MAX_ACCOUNT_DRAWDOWN = 0.05       # 5%
MAX_DAILY_LOSS = 0.03             # 3%

MAX_OPEN_POSITIONS = 2

RISK_PER_TRADE_USD = 12

LEVERAGE = 200

MAX_MARGIN_USAGE = 0.80


# =====================================================
# TRADING TIME
# =====================================================

TRADING_START_HOUR = 23           # 11 PM IST

TRADING_END_HOUR = 11             # Next day

ALLOW_HOLD_TO_EXPIRY = True

FORCE_EXIT_MINUTES_BEFORE_EXPIRY = 5

NO_NEW_TRADE_LAST_MINUTES = 30


# =====================================================
# OPTION FILTERS
# =====================================================

TARGET_DTE = 1

OPTION_TYPES = [
    "call_options",
    "put_options",
]

PREMIUM_MIN = 12

PREMIUM_MAX = 30

DELTA_MIN = 0.02

DELTA_MAX = 0.04

MAX_GAMMA = 0.002

MAX_VEGA = 25

MIN_THETA = -8


# =====================================================
# LIQUIDITY FILTERS
# =====================================================

MIN_OPEN_INTEREST = 500

MIN_VOLUME = 20

MAX_SPREAD_PERCENT = 5

MIN_BID_SIZE = 100

MIN_ASK_SIZE = 100


# =====================================================
# PREMIUM TRACKER
# =====================================================

PREMIUM_LOOKBACK_MINUTES = 240

MIN_PREMIUM_EXPANSION = 4.0

MAX_PREMIUM_EXPANSION = 8.0

MIN_PREMIUM_DECAY = 0.50

MINUTES_AFTER_LOW = 20


# =====================================================
# BTC MARKET FILTERS
# =====================================================

EMA_FAST = 20

EMA_SLOW = 50

EMA_LONG = 200

RSI_PERIOD = 14

RSI_OVERSOLD = 30

RSI_OVERBOUGHT = 70

ADX_PERIOD = 14

ADX_MIN = 20

ATR_PERIOD = 14

MAX_ATR_PERCENT = 0.80

MAX_DAILY_BTC_MOVE = 3.5


# =====================================================
# VOLATILITY
# =====================================================

MIN_IV = 0.20

MAX_IV = 0.80

MIN_HV = 0.01

MAX_HV = 0.45

MAX_IV_EXPANSION = 15


# =====================================================
# MARKET REGIME
# =====================================================

ALLOW_STRONG_UPTREND = False

ALLOW_WEAK_UPTREND = False

ALLOW_SIDEWAYS = True

ALLOW_VOLATILE_RANGE = False

ALLOW_STRONG_DOWNTREND = False

ALLOW_PANIC_SELLING = False


# =====================================================
# EXECUTION
# =====================================================

LIMIT_ORDER_ONLY = True

LIMIT_TIMEOUT = 15

MAX_SLIPPAGE = 0.30

RETRY_LIMIT_ORDER = 3

ALLOW_PARTIAL_FILL = True


# =====================================================
# EXIT RULES
# =====================================================

STOP_LOSS_USD = 15

TARGET_PROFIT_PERCENT = 60

EXIT_ON_DELTA = 0.10

EXIT_ON_IV_SPIKE = True

EXIT_ON_MARGIN_WARNING = True

EXIT_ON_BTC_BREAKOUT = True


# =====================================================
# SCORING ENGINE
# =====================================================

MINIMUM_SCORE = 85

TREND_WEIGHT = 15

REVERSAL_WEIGHT = 20

PREMIUM_WEIGHT = 20

THETA_WEIGHT = 15

DELTA_WEIGHT = 10

LIQUIDITY_WEIGHT = 10

VOLATILITY_WEIGHT = 5

ATR_WEIGHT = 5


# =====================================================
# BACKTEST
# =====================================================

MAKER_FEE = 0.00015

TAKER_FEE = 0.00015

SIMULATED_SLIPPAGE = 0.05

SIMULATE_PARTIAL_FILL = True

SAVE_ALL_TRADES = True


# =====================================================
# LOGGING
# =====================================================

PRINT_SIGNALS = True

PRINT_TRADES = True

PRINT_REJECTIONS = True

SAVE_LOGS = True

DEBUG_MODE = False

# =====================================================
# ADVANCED FILTERS
# =====================================================

USE_THETA_EFFICIENCY = True

MIN_THETA_EFFICIENCY = 0.80

USE_ORDERBOOK_IMBALANCE = True

MIN_BUY_SELL_RATIO = 1.20

USE_PREMIUM_ACCELERATION = True

MIN_PREMIUM_ACCELERATION = 0.25

USE_DYNAMIC_STOPLOSS = True

USE_DYNAMIC_POSITION_SIZE = True

USE_DYNAMIC_DELTA_FILTER = True

AVOID_EXTREME_IV = True

AVOID_HIGH_VOLATILITY_DAYS = True

AVOID_WEEKLY_EXPIRY_IF_BTC_MOVE_GT = 4.0

ENABLE_MARKET_REGIME_FILTER = True

ENABLE_LIQUIDITY_SCORE = True

ENABLE_OPTION_SCORE = True

ENABLE_PORTFOLIO_RISK_CHECK = True