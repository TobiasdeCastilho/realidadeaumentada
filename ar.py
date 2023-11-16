import time
import cv2 as cv
import numpy as num

def arShow(dictionary: int, capture: cv.VideoCapture, windowSize: [int, int], definitions: [{"id": int, "image": [any]}], frameRate: int = 24):
  detector = cv.aruco.ArucoDetector(cv.aruco.getPredefinedDictionary(dictionary))

  if (not capture.isOpened):
    raise IOError("Cannot open cam")
  
  indG = 0
  milliseconds = int(time.time() * 1000)

  at = {}
  for de1finition in definitions:      
    at[de1finition["id"]] = 0  

  while True:         
    indG = 0   
    newMiliseconds = int(time.time() * 1000)    
    if((newMiliseconds - milliseconds) > (1000 / frameRate)):                
        milliseconds = newMiliseconds          
        indG = 1                

    _, window = capture.read()
    window = cv.resize(window, windowSize, fx=.5, fy=.5,
                       interpolation=cv.INTER_AREA)
    
    (corners, ids, _) = detector.detectMarkers(window)
    
    [windowH, windowW] = window.shape[:2]

    refs = []
    if len(corners) > 0:
      for definition in definitions:
        j = num.squeeze(num.where(ids == definition["id"]))
        if j.size > 0:                                                   
          refs.append({"id": definition["id"],"corner": num.squeeze(corners[int(j[0])]), "image": definition["image"]})
      
      for ref in refs:
        (tl, tr, bl, br) = ref["corner"]                    
        matrix = num.array([tl, tr, bl, br])
    
        at[ref["id"]] += indG
        if(at[ref["id"]] >= len(ref["image"])):
          at[ref["id"]] = 0
        source = ref["image"][at[ref["id"]]]

        (matrixH, matrixW) = source.shape[:2]            
        sourceMatrix = num.array([[0, 0], [matrixW, 0], [matrixW, matrixH], [0, matrixH]])

        (H, _) = cv.findHomography(sourceMatrix, matrix)

        warped = cv.warpPerspective(source, H, (windowW, windowH))            

        windowMask = num.zeros((windowH, windowW), dtype="uint8")
        cv.fillConvexPoly(windowMask,
                          matrix.astype("int32"),
                          (255, 255, 255),
                          cv.LINE_AA)
        
        windowMaskScaled = windowMask.copy() / 255.0
        windowMaskScaled = num.dstack([windowMaskScaled] * 3)

        warpedMultiplied = cv.multiply(warped.astype("float"), windowMaskScaled)

        captureMultiplied = cv.multiply(window.astype("float"), 1.0 - windowMaskScaled)

        window = cv.add(warpedMultiplied, captureMultiplied)
        window = window.astype("uint8")
    
    cv.imshow('test', window)
    cv.waitKey(1)