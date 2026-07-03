import numpy as np
import pandas as pd


# =====================================================
# MOVING AVERAGES
# =====================================================

def sma(series, period):

    return series.rolling(period).mean()


def ema(series, period):

    return series.ewm(

        span=period,

        adjust=False,

    ).mean()


def wma(series, period):

    weights = np.arange(1, period + 1)

    return series.rolling(period).apply(

        lambda prices: np.dot(prices, weights) / weights.sum(),

        raw=True,

    )


# =====================================================
# TRUE RANGE
# =====================================================

def true_range(df):

    high_low = df["high"] - df["low"]

    high_close = (

        df["high"]

        - df["close"].shift()

    ).abs()

    low_close = (

        df["low"]

        - df["close"].shift()

    ).abs()

    tr = pd.concat(

        [

            high_low,

            high_close,

            low_close,

        ],

        axis=1,

    ).max(axis=1)

    return tr


def atr(

    df,

    period=14,

):

    tr = true_range(df)

    return tr.rolling(period).mean()


# =====================================================
# RETURNS
# =====================================================

def log_returns(df):

    return np.log(

        df["close"]

        /

        df["close"].shift(1)

    )


def historical_volatility(

    df,

    period=30,

):

    returns = log_returns(df)

    return (

        returns

        .rolling(period)

        .std()

        * np.sqrt(365)

    )


# =====================================================
# RSI
# =====================================================

def rsi(

    series,

    period=14,

):

    delta = series.diff()

    gain = delta.where(

        delta > 0,

        0,

    )

    loss = -delta.where(

        delta < 0,

        0,

    )

    avg_gain = gain.rolling(period).mean()

    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    return 100 - (

        100 / (1 + rs)

    )


# =====================================================
# MACD
# =====================================================

def macd(

    series,

    fast=12,

    slow=26,

    signal=9,

):

    ema_fast = ema(

        series,

        fast,

    )

    ema_slow = ema(

        series,

        slow,

    )

    macd_line = ema_fast - ema_slow

    signal_line = ema(

        macd_line,

        signal,

    )

    histogram = (

        macd_line

        - signal_line

    )

    return {

        "macd": macd_line,

        "signal": signal_line,

        "histogram": histogram,

    }


# =====================================================
# VWAP
# =====================================================

def vwap(df):

    tp = (

        df["high"]

        + df["low"]

        + df["close"]

    ) / 3

    return (

        tp * df["volume"]

    ).cumsum() / (

        df["volume"].cumsum()

    )


# =====================================================
# VOLUME SMA
# =====================================================

def volume_sma(

    df,

    period=20,

):

    return (

        df["volume"]

        .rolling(period)

        .mean()

    )


# =====================================================
# BOLLINGER BANDS
# =====================================================

def bollinger_bands(

    series,

    period=20,

    std_dev=2,

):

    middle = sma(

        series,

        period,

    )

    std = (

        series

        .rolling(period)

        .std()

    )

    upper = middle + std_dev * std

    lower = middle - std_dev * std

    return {

        "upper": upper,

        "middle": middle,

        "lower": lower,

    }
# =====================================================
# PRICE UTILITIES
# =====================================================

def highest(series, period=20):

    return series.rolling(period).max()


def lowest(series, period=20):

    return series.rolling(period).min()


def rolling_std(series, period=20):

    return series.rolling(period).std()


# =====================================================
# TREND UTILITIES
# =====================================================

def slope(series, period=5):

    """
    Returns the slope over the last 'period' values.
    Positive = rising
    Negative = falling
    """

    return series.diff(period) / period


def ema_distance(price, ema_series):

    """
    Percentage distance from EMA.
    """

    return ((price - ema_series) / ema_series) * 100


def trend_strength(ema_fast, ema_slow):

    """
    Percentage difference between two EMAs.
    """

    return ((ema_fast - ema_slow) / ema_slow) * 100


# =====================================================
# HIGH / LOW DETECTION
# =====================================================

def higher_high(df, lookback=3):

    highs = df["high"].tail(lookback)

    return highs.iloc[-1] > highs.iloc[:-1].max()


def lower_low(df, lookback=3):

    lows = df["low"].tail(lookback)

    return lows.iloc[-1] < lows.iloc[:-1].min()


def higher_low(df, lookback=3):

    lows = df["low"].tail(lookback)

    return lows.iloc[-1] > lows.iloc[:-1].min()


def lower_high(df, lookback=3):

    highs = df["high"].tail(lookback)

    return highs.iloc[-1] < highs.iloc[:-1].max()


# =====================================================
# CROSSOVER DETECTION
# =====================================================

def cross_above(series1, series2):

    if len(series1) < 2 or len(series2) < 2:
        return False

    return (

        series1.iloc[-2] <= series2.iloc[-2]

        and

        series1.iloc[-1] > series2.iloc[-1]

    )


def cross_below(series1, series2):

    if len(series1) < 2 or len(series2) < 2:
        return False

    return (

        series1.iloc[-2] >= series2.iloc[-2]

        and

        series1.iloc[-1] < series2.iloc[-1]

    )


# =====================================================
# PRICE POSITION
# =====================================================

def price_above(price, level):

    return price > level


def price_below(price, level):

    return price < level


# =====================================================
# VOLATILITY HELPERS
# =====================================================

def atr_percent(df, period=14):

    atr_values = atr(df, period)

    return (atr_values / df["close"]) * 100


def realized_volatility(df, period=30):

    returns = log_returns(df)

    return returns.rolling(period).std() * np.sqrt(365)


# =====================================================
# SIMPLE MARKET STATE
# =====================================================

def market_state(ema20, ema50, hv):

    if ema20 > ema50 and hv < 0.60:

        return "TRENDING"

    if ema20 < ema50 and hv < 0.60:

        return "DOWNTREND"

    if hv >= 0.60:

        return "VOLATILE"

    return "RANGING"


# =====================================================
# NORMALIZATION
# =====================================================

def normalize(value, minimum, maximum):

    if maximum == minimum:

        return 0

    value = max(minimum, min(value, maximum))

    return (value - minimum) / (maximum - minimum)


# =====================================================
# SCORE CLAMP
# =====================================================

def clamp(score, minimum=0, maximum=100):

    return max(minimum, min(score, maximum))