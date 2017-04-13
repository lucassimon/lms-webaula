# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from lmswebaula.lms.core.containers.login import LoginRQ

from lmswebaula.lms.student.containers import *

from lmswebaula.lms.student.rpc import (
    RPC as StudentRPC
)

from lmswebaula.lms.student.containers.students import (
    StudentRS
)

from lmswebaula.lms.student.parse import (
    StudentParse
)


class API(object):
    """
    Api para servico com a solução LMS do WebAula

    Produto: http://lmsenterprise.webaula.com.br/

    Url: http://lmsapi.webaula.com.br/v3/DOC/API.aspx

    """

    ENDPOINT = 'http://lmsapi.webaula.com.br/v3/Student.svc?singleWsdl'

    def __init__(self, passport):

        login = LoginRQ(passport, url=self.ENDPOINT)

        self.rpc = StudentRPC(
            login=login,
            passport=passport
        )

    def _verifica_exception(self, res, execption_class=Exception):

        if res['hasError']:
            raise execption_class(res['Msg'])

    def get_all(self, paginate_rq):
        """
        Retorna todos os estudantes
        """

        if not isinstance(paginate_rq, GetAllRQ):
            raise ValueError(
                "Não existe uma instancia para os dados da paginação"
            )

        try:
            response = self.rpc.get_all(paginate_rq)
        except Exception as e:
            raise e

        # Verificar se tem erro na resposta

        self._verifica_exception(response)

        # tratar os dados

        students = StudentParse.get_all(response)

        # Retornar o student response

        return students

    def save(self, student_rq):
        """
        Cria/Atualiza um aluno
        """

        if not isinstance(student_rq, StudentDTO):
            raise ValueError(
                "Não existe uma instância para os dados do estudante"
            )

        try:
            response = self.rpc.save(student_rq)
        except Exception as e:
            raise e

        self._verifica_exception(response)

        result = StudentRS()

        return result