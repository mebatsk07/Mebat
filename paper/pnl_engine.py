class PnLEngine:

    def calculate_short_option_pnl(

        self,

        entry,

        current,

        qty,

    ):

        return (

            entry

            - current

        ) * qty