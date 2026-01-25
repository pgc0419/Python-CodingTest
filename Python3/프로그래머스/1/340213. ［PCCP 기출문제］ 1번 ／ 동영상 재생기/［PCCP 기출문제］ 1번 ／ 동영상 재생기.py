def to_seconds(pos):
    m, s = map(int, pos.split(":"))
    return m * 60 + s

def to_string(seconds):
    m = seconds // 60
    s = seconds % 60
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)
    
    def skip_opening(pos):
        if op_start <= pos <= op_end:
            return op_end
        return pos
    
    pos = skip_opening(pos)
    
    for cmd in commands:
        if cmd == "next":
            pos = min(video_len, pos + 10)
        elif cmd == "prev":
            pos = max(0, pos - 10)
        
        pos = skip_opening(pos)
            
    return to_string(pos)