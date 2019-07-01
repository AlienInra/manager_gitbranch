# -*- coding: UTF-8 -*-
# author:liujiayu

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired

class branchForm(FlaskForm):
    model = SelectMultipleField(
        label="下拉菜单",
        validators=[
            DataRequired("下拉菜单")
        ],
        render_kw={
            "class": "form-control selectpicker",
            "title": "请选择模块名称"
        },
        choices=[],
        default=1,
        coerce=int
    )
    branch_base = StringField(
        label="基础分支",
        validators=[
            DataRequired("请输入基础分支名称")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "基础分支名称"
        }
    )
    branch_to = StringField(
        label="目标分支",
        validators=[
            DataRequired("请输入目标分支名称")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "目标分支名称"
        }
    )

    submit = SubmitField(
        label="确认",
        render_kw={
            "class": "btn btn-primary"
        }

    )
class addForm(FlaskForm):
    model_name = StringField(
        label="模块名称",
        validators=[
            DataRequired("请输入模块名称")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "group/project"
        }
    )

    submit = SubmitField(
        label="确认",
        render_kw={
            "class": "btn btn-primary"
        }

    )

class delForm(FlaskForm):
    submit = SubmitField(
        label="返回",
        render_kw={
            "class": "btn btn-primary"
        }

    )


