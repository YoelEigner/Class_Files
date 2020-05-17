properties([parameters([string(defaultValue: '24', description: '', name: 'NAME', trim: false)]), pipelineTriggers([pollSCM('* * * * *')])])

node{
    stage("clone"){
        git "https://github.com/YoelEigner/Class_Files.git"
    }
    stage("show"){
        bat "dir"
    }
	    stage("print"){
        bat "echo All done"
    }
}