# -*- coding: UTF-8 -*-
# author:liujiayu
import gitlab.v4.objects

class gitlabAPI():
    def __init__(self):
        self.url = 'xxxxxxxxxxxxx'
        self.gl = gitlab.Gitlab(self.url, private_token='xxxxxxxxxxxxx')
    #创建分支
    def make_branch(self, to_branch, base_branch, proj):
        project = self.gl.projects.get(proj)
        true_or_flase=project.branches.create({'branch': to_branch, 'ref': base_branch})

        if true_or_flase:
            return True
        else:
            return False

    #获取项目全部分支
    def all_branch(self, proj,to_branch):
        project_branch=[] # ['master','dev'...]
        project_branch_dict_all={} # {'group/project':['master','develop']}
        status_branch = []
        project_branch_dict = {} # {'group/project':['master','失败']}
        project = self.gl.projects.get(proj)
        branches = project.branches.list()
        for branch in branches:
            project_branch.append(branch.name)
        project_branch_dict_all[proj]=project_branch

        for branch in project_branch_dict_all:
            if to_branch in project_branch_dict_all[branch]:
                status_branch.append(to_branch)
                status_branch.append("成功")
            else:
                status_branch.append(to_branch)
                status_branch.append("失败")

        project_branch_dict[proj]=status_branch
        return project_branch_dict
    #获取项目对象
    def get_project(self,proj):
        project = self.gl.projects.get(proj)
        return project
    #保护为40:master
    def to_40_project(self,proj,to_branch):
        project = self.gl.projects.get(proj)
        branch = project.branches.get(to_branch)
        branch.protect()
    #保护为0:no one
    def to_0_project(self,proj,to_branch):
        project = self.gl.projects.get(proj)
        p_branch=project.protectedbranches.create({
            'name':to_branch,
            'merge_access_level':0,
            'push_access_level':0
        })