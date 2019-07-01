from flask import render_template, flash, redirect, url_for
from app.web.forms import branchForm, addForm, delForm
from gitlab_api import gitlabAPI
from . import web
from app.models import Model_name, Model_status
from app import db

@web.route('/list', methods=['GET','POST'])
def list():
    form = delForm()
    data = Model_status.query.all()
    if form.validate_on_submit():
        for i in data:
            db.session.delete(i)
            db.session.commit()
        return redirect(url_for("web.branch_manage"))
    return render_template("list.html",data=data,form=form)


@web.route('/', methods=['GET', 'POST'])
def branch_manage():
    form = branchForm()
    form.model.choices =[(v.id,v.model_name) for v in Model_name.query.all()]
    try:
        if form.validate_on_submit():
            data = form.data
            brch = gitlabAPI()
            model_dict = {}
            model_choose = {}  # {1: 'group1/project1', 2: 'group2/project2'}
            model_query = Model_name.query.all()
            for v in model_query:
                model_choose[v.id]=v.model_name
            for id in data["model"]:
                model_dict[id] = model_choose[id]
            for i in model_dict:
                ret = brch.make_branch(data["branch_to"], data["branch_base"], model_dict[i])
                brch.to_0_project(model_dict[i],data["branch_to"])
                if ret == True:
                    info = Model_status(
                        model_name=model_dict[i],
                        base_name=data["branch_base"],
                        to_branch=data["branch_to"],
                        status="成功"
                    )
                    db.session.add(info)
                    db.session.commit()

            return redirect(url_for("web.list"))
    except Exception as e:
        print(str(e))
        flash("错误：{}".format(str(e)), "err")

    return render_template("branch_manage.html", form=form)


@web.route('/branch_add', methods=['GET', 'POST'])
def branch_add():
    form = addForm()
    try:
        if form.validate_on_submit():
            data=form.data
            brch = gitlabAPI()
            ret=brch.get_project(data["model_name"])
            if ret:
                data_model=Model_name(model_name=data["model_name"])
                db.session.add(data_model)
                db.session.commit()
                flash("添加成功", "ok")
                return redirect(url_for("web.branch_manage"))
    except Exception as e:
        print(str(e))
        flash("错误：{}".format(str(e)), "err")
    return render_template("branch_add.html",form=form)



