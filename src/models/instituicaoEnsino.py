class InstituicaoEnsino:
    def __init__(
        self,
        no_entidade,
        co_entidade,
        no_uf,
        sg_uf,
        co_uf,
        no_municipio,
        co_municipio,
        no_mesorregiao,
        co_mesorregiao,
        no_microrregiao,
        co_microrregiao,
        nu_ano_censo,
        no_regiao,
        co_regiao,
        qt_mat_bas,
        qt_mat_inf,
        qt_mat_fund,
        qt_mat_med,
        qt_mat_prof,
        qt_mat_eja,
        qt_mat_esp
    ):
        self.no_entidade = no_entidade
        self.co_entidade = co_entidade
        self.no_uf = no_uf
        self.sg_uf = sg_uf
        self.co_uf = co_uf
        self.no_municipio = no_municipio
        self.co_municipio = co_municipio
        self.no_mesorregiao = no_mesorregiao
        self.co_mesorregiao = co_mesorregiao
        self.no_microrregiao = no_microrregiao
        self.co_microrregiao = co_microrregiao
        self.nu_ano_censo = nu_ano_censo
        self.no_regiao = no_regiao
        self.co_regiao = co_regiao
        self.qt_mat_bas = qt_mat_bas
        self.qt_mat_inf = qt_mat_inf
        self.qt_mat_fund = qt_mat_fund
        self.qt_mat_med = qt_mat_med
        self.qt_mat_prof = qt_mat_prof
        self.qt_mat_eja = qt_mat_eja
        self.qt_mat_esp = qt_mat_esp

    def to_dict(self):
        return {
            "no_entidade": self.no_entidade,
            "co_entidade": self.co_entidade,
            "no_uf": self.no_uf,
            "sg_uf": self.sg_uf,
            "co_uf": self.co_uf,
            "no_municipio": self.no_municipio,
            "co_municipio": self.co_municipio,
            "no_mesorregiao": self.no_mesorregiao,
            "co_mesorregiao": self.co_mesorregiao,
            "no_microrregiao": self.no_microrregiao,
            "co_microrregiao": self.co_microrregiao,
            "nu_ano_censo": self.nu_ano_censo,
            "no_regiao": self.no_regiao,
            "co_regiao": self.co_regiao,
            "qt_mat_bas": self.qt_mat_bas,
            "qt_mat_inf": self.qt_mat_inf,
            "qt_mat_fund": self.qt_mat_fund,
            "qt_mat_med": self.qt_mat_med,
            "qt_mat_prof": self.qt_mat_prof,
            "qt_mat_eja": self.qt_mat_eja,
            "qt_mat_esp": self.qt_mat_esp
        }


    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["no_entidade"],
            dados["co_entidade"],
            dados["no_uf"],
            dados["sg_uf"],
            dados["co_uf"],
            dados["no_municipio"],
            dados["co_municipio"],
            dados["no_mesorregiao"],
            dados["co_mesorregiao"],
            dados["no_microrregiao"],
            dados["co_microrregiao"],
            dados["nu_ano_censo"],
            dados["no_regiao"],
            dados["co_regiao"],
            dados["qt_mat_bas"],
            dados["qt_mat_inf"],
            dados["qt_mat_fund"],
            dados["qt_mat_med"],
            dados["qt_mat_prof"],
            dados["qt_mat_eja"],
            dados["qt_mat_esp"]
        )