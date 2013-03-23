#encoding:utf-8
from reaper_python import *



def printf(agr):
    RPR_ShowConsoleMsg(str(agr)+'\n')
    pass


def cmd(cmdId):
    RPR_Main_OnCommand(cmdId, 0)
    pass


def record_arm(trk, state=1):
    RPR_SetMediaTrackInfo_Value(trk, 'I_RECARM', state)


def record_unarm(trk):
    record_arm(trk, state=0)


if __name__ == '__main__':


    CMD_Trk_Monitor_On = 40493
    CMD_Trk_Monitor_Off = 40492
    CMD_Show_KB = 40377
    CMD_Unarmed_all = 40491
    cmd(CMD_Unarmed_all)
    Trk_Select = RPR_GetSelectedTrack(0, 0)
    trkState, d, flag = RPR_GetTrackState(Trk_Select, 0)
    isArmed = flag & 64
    if isArmed:
        record_unarm(Trk_Select)
        cmd(CMD_Trk_Monitor_Off)
    else:
        record_arm(Trk_Select)
        cmd(CMD_Trk_Monitor_On)
    cmd(CMD_Show_KB)
    printf(flag)
