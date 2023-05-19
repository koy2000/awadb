# automatically generated by the FlatBuffers compiler, do not modify

# namespace: gamma_api

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class EngineStatus(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = EngineStatus()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsEngineStatus(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # EngineStatus
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # EngineStatus
    def IndexStatus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EngineStatus
    def TableMem(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EngineStatus
    def IndexMem(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EngineStatus
    def VectorMem(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EngineStatus
    def FieldRangeMem(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EngineStatus
    def BitmapMem(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int64Flags, o + self._tab.Pos)
        return 0

    # EngineStatus
    def DocNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EngineStatus
    def MaxDocid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # EngineStatus
    def MinIndexedNum(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(9)
def EngineStatusStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddIndexStatus(builder, indexStatus): builder.PrependInt32Slot(0, indexStatus, 0)
def EngineStatusAddIndexStatus(builder, indexStatus):
    """This method is deprecated. Please switch to AddIndexStatus."""
    return AddIndexStatus(builder, indexStatus)
def AddTableMem(builder, tableMem): builder.PrependInt64Slot(1, tableMem, 0)
def EngineStatusAddTableMem(builder, tableMem):
    """This method is deprecated. Please switch to AddTableMem."""
    return AddTableMem(builder, tableMem)
def AddIndexMem(builder, indexMem): builder.PrependInt64Slot(2, indexMem, 0)
def EngineStatusAddIndexMem(builder, indexMem):
    """This method is deprecated. Please switch to AddIndexMem."""
    return AddIndexMem(builder, indexMem)
def AddVectorMem(builder, vectorMem): builder.PrependInt64Slot(3, vectorMem, 0)
def EngineStatusAddVectorMem(builder, vectorMem):
    """This method is deprecated. Please switch to AddVectorMem."""
    return AddVectorMem(builder, vectorMem)
def AddFieldRangeMem(builder, fieldRangeMem): builder.PrependInt64Slot(4, fieldRangeMem, 0)
def EngineStatusAddFieldRangeMem(builder, fieldRangeMem):
    """This method is deprecated. Please switch to AddFieldRangeMem."""
    return AddFieldRangeMem(builder, fieldRangeMem)
def AddBitmapMem(builder, bitmapMem): builder.PrependInt64Slot(5, bitmapMem, 0)
def EngineStatusAddBitmapMem(builder, bitmapMem):
    """This method is deprecated. Please switch to AddBitmapMem."""
    return AddBitmapMem(builder, bitmapMem)
def AddDocNum(builder, docNum): builder.PrependInt32Slot(6, docNum, 0)
def EngineStatusAddDocNum(builder, docNum):
    """This method is deprecated. Please switch to AddDocNum."""
    return AddDocNum(builder, docNum)
def AddMaxDocid(builder, maxDocid): builder.PrependInt32Slot(7, maxDocid, 0)
def EngineStatusAddMaxDocid(builder, maxDocid):
    """This method is deprecated. Please switch to AddMaxDocid."""
    return AddMaxDocid(builder, maxDocid)
def AddMinIndexedNum(builder, minIndexedNum): builder.PrependInt32Slot(8, minIndexedNum, 0)
def EngineStatusAddMinIndexedNum(builder, minIndexedNum):
    """This method is deprecated. Please switch to AddMinIndexedNum."""
    return AddMinIndexedNum(builder, minIndexedNum)
def End(builder): return builder.EndObject()
def EngineStatusEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)